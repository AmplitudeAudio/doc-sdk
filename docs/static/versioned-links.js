/**
 * Runtime rewriting of SDK source-code links so they point to the GitHub
 * branch/tag that matches the current Mike documentation version.
 *
 * Build-time replacement (via hooks/mkdoxy_param_direction.py) provides a
 * fallback default (usually "develop"). This script corrects those links
 * when the user is viewing a specific version such as "v1.x" or "stable".
 *
 * Versioning scheme
 *   - Docs track "stream" versions: v1.x, v2.x, etc. (each maps 1:1 to a
 *     matching GitHub branch: v1.x → v1.x, v2.x → v2.x).
 *   - Minor/patch releases (v1.0.0, v1.1.0, …) are git tags only; they do
 *     not have dedicated documentation sites.
 *   - "nightly" docs map to the develop branch.
 *   - "stable" docs map to the main branch.
 *
 * Mapping rules
 * - "nightly" → "develop" branch
 * - "stable"  → "main" branch
 * - "vN.x"    → "vN.x" branch (1:1)
 * - Aliases are resolved via /versions.json first, but the explicit rules
 *   above take precedence.
 */
(function () {
    'use strict';

    /**
     * Extract the Mike version slug from the URL path.
     * Mike deploys versioned sites under /{version}/.
     */
    function getCurrentVersion() {
        const m = window.location.pathname.match(/^\/([^/]+)\//);
        return m ? m[1] : null;
    }

    /**
     * Resolve a documentation version to the corresponding GitHub branch/tag.
     * Aliases are looked up in Mike's versions.json.
     */
    async function resolveBranch(version) {
        if (!version) {
            return null;
        }

        try {
            const response = await fetch('/versions.json');
            if (response.ok) {
                const versions = await response.json();
                const entry = versions.find(
                    (v) => Array.isArray(v.aliases) && v.aliases.includes(version)
                );
                if (entry && entry.version) {
                    version = entry.version;
                }
            }
        } catch (_e) {
            // Ignore network/fetch errors; continue with raw version name.
        }

        if (version === 'nightly') {
            return 'develop';
        }

        if (version === 'stable') {
            return 'main';
        }

        return version;
    }

    /**
     * Rewrite every GitHub SDK blob link to use the resolved branch.
     */
    function rewriteLinks(branch) {
        if (!branch) {
            return;
        }

        const selector = 'a[href*="github.com/AmplitudeAudio/sdk/blob/"]';
        document.querySelectorAll(selector).forEach((link) => {
            try {
                const url = new URL(link.href);
                const parts = url.pathname.split('/');
                const blobIndex = parts.indexOf('blob');
                if (blobIndex !== -1 && parts[blobIndex + 1] !== undefined) {
                    parts[blobIndex + 1] = branch;
                    url.pathname = parts.join('/');
                    link.href = url.toString();
                }
            } catch (_e) {
                // Skip malformed URLs.
            }
        });
    }

    async function init() {
        const version = getCurrentVersion();
        if (!version) {
            // No version prefix in URL (e.g. local `properdocs serve`).
            // Leave the build-time fallback links untouched.
            return;
        }
        const branch = await resolveBranch(version);
        if (branch) {
            rewriteLinks(branch);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
