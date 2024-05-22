document.addEventListener("DOMContentLoaded", function() {
    const faqItems = document.querySelectorAll(".faq-question");

    faqItems.forEach(item => {
        item.addEventListener("click", function() {
            this.classList.toggle("active");
            const answer = this.nextElementSibling;
            if (answer.style.maxHeight) {
                answer.style.maxHeight = null;
            } else {
                answer.style.maxHeight = answer.scrollHeight + "px";
            }
        });
    });
});
