const button = document.querySelector("button");
const textarea = document.querySelector("textarea");
const postList = document.querySelector(".post-list");

button.addEventListener("click", () => {

    const text = textarea.value.trim();

    if(text === ""){
        alert("글을 입력해주세요!");
        return;
    }

    const post = document.createElement("article");

    post.className = "post";

    post.innerHTML = `
        <div class="post-header">
            <span class="nickname">익명</span>
            <span class="date">2026.05.22</span>
        </div>

<details>

    <summary class="title">
        📌 ${text.substring(0, 10)}...
    </summary>

    <p class="content">
        ${text}
    </p>

</details>    `;

    postList.prepend(post);

    textarea.value = "";
});