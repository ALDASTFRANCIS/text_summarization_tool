const links = document.querySelectorAll("a");

links.forEach((link) => {
    if (link.innerText.length > 15) {
        createBusterButton(link);
    }
});

function createBusterButton(linkElement) {
    const btn = document.createElement("button");
    btn.innerText = "🤖"; 
    btn.className = "clickbait-buster-btn";
    btn.style.marginLeft = "5px";
    btn.style.cursor = "pointer";
    btn.style.border = "none";
    btn.style.background = "transparent";

    btn.onclick = (e) => {
        e.preventDefault();
        btn.innerText = "⏳";

        chrome.runtime.sendMessage(
            { action: "summarize", url: linkElement.href },
            (response) => {

                if (response && response.success) {

                    linkElement.innerText = response.data.summary;
                    linkElement.style.color = "green";
                    linkElement.style.fontWeight = "bold";
                    btn.remove();
                } else {

                    console.error("Background script error:", response.error);
                    btn.innerText = "❌"; 
                }
            }
        );
    };

    linkElement.parentNode.insertBefore(btn, linkElement.nextSibling);
}