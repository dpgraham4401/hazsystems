// https://docs.readthedocs.com/platform/stable/intro/mkdocs.html#configure-read-the-docs-search
document.addEventListener("DOMContentLoaded", function(event) {
// Trigger Read the Docs' search addon instead of Material MkDocs default
document.querySelector(".md-search__input").addEventListener("focus", (e) => {
        const event = new CustomEvent("readthedocs-search-show");
        document.dispatchEvent(event);
    });
});