var consent = __md_get("__consent")
if (consent && consent.clarity) {
    window.clarity('consent');
} else {
    window.clarity('consent', false);
}