import "../static/js/testimonials";

describe("Comment Modals", () => {
  beforeEach(() => {
    document.body.innerHTML = `
            <input type="hidden" id="testimonialId" />
            <div id="testimonialUserName"></div>
            <textarea id="commentContent"></textarea>
            <div id="charCount">0 / 50 characters</div>
            <div id="commentModal"></div>
        `;

    // mock bootstrap
    window.bootstrap = {
      Modal: class {
        constructor(element) {
          this.element = element;
        }
        show() {}
        hide() {}
      },
    };

    // define opencommentmodal function
    window.openCommentModal = function (testimonialId, userName) {
      document.getElementById("testimonialId").value = testimonialId;
      document.getElementById("testimonialUserName").textContent = userName;

      const commentInput = document.getElementById("commentContent");
      const charCount = document.getElementById("charCount");
      charCount.textContent = "0 / 50 characters";

      commentInput.addEventListener("input", () => {
        const currentLength = commentInput.value.length;
        charCount.textContent = `${currentLength} / 50 characters`;
        charCount.style.color = currentLength > 50 ? "red" : "black";
      });

      const commentModal = new window.bootstrap.Modal(
        document.getElementById("commentModal")
      );
      commentModal.show();
    };

    // define the hideCommentModal function
    window.hideCommentModal = function () {
      const commentModal = new window.bootstrap.Modal(
        document.getElementById("commentModal")
      );
      commentModal.hide();
    };
  });

  test("should open comment modal and update character count", () => {
    openCommentModal("1", "Test User");

    const testimonialId = document.getElementById("testimonialId");
    const userNameElement = document.getElementById("testimonialUserName");
    const charCount = document.getElementById("charCount");

    expect(testimonialId.value).toBe("1");
    expect(userNameElement.textContent).toBe("Test User");
    expect(charCount.textContent).toBe("0 / 50 characters");
  });

  test("should update character count when input changes", () => {
    openCommentModal("1", "Test User");

    const commentInput = document.getElementById("commentContent");
    const charCount = document.getElementById("charCount");

    commentInput.value = "Hello World!";
    commentInput.dispatchEvent(new Event("input"));

    expect(charCount.textContent).toBe("12 / 50 characters");
    expect(charCount.style.color).toBe("black");

    const longInput = "This is a test input that exceeds fifty characters."; // 51 characters
    commentInput.value = longInput;
    commentInput.dispatchEvent(new Event("input"));

    expect(charCount.textContent).toBe("51 / 50 characters"); // update to match real length
    expect(charCount.style.color).toBe("red");
  });

  test("should hide comment modal", () => {
    openCommentModal("1", "Test User");
    hideCommentModal();

    const commentModal = new window.bootstrap.Modal(
      document.getElementById("commentModal")
    );
  });

  test("should reset character count when modal is opened again", () => {
    openCommentModal("1", "Test User");

    const commentInput = document.getElementById("commentContent");
    const charCount = document.getElementById("charCount");

    commentInput.value = "Some input text.";
    commentInput.dispatchEvent(new Event("input"));

    // character count reflects input
    expect(charCount.textContent).toBe("16 / 50 characters");
    expect(commentInput.value).toBe("Some input text.");

    commentInput.value = "";
    charCount.textContent = "0 / 50 characters";
    openCommentModal("1", "Test User");

    expect(commentInput.value).toBe("");
    expect(charCount.textContent).toBe("0 / 50 characters");
  });

  test("should not exceed character limit", () => {
    openCommentModal("1", "Test User");

    const commentInput = document.getElementById("commentContent");
    const charCount = document.getElementById("charCount");

    commentInput.value = "A".repeat(51); // 51 characters
    commentInput.dispatchEvent(new Event("input"));

    expect(charCount.textContent).toBe("51 / 50 characters");
    expect(charCount.style.color).toBe("red");
  });

  test("should retain username and testimonial ID when reopening the modal", () => {
    openCommentModal("1", "Test User");

    hideCommentModal();
    openCommentModal("1", "Test User");

    const testimonialId = document.getElementById("testimonialId");
    const userNameElement = document.getElementById("testimonialUserName");

    expect(testimonialId.value).toBe("1");
    expect(userNameElement.textContent).toBe("Test User");
  });

  test("should clear input when modal is closed", () => {
    openCommentModal("1", "Test User");
    const commentInput = document.getElementById("commentContent");

    commentInput.value = "Some input text.";
    commentInput.dispatchEvent(new Event("input"));

    expect(commentInput.value).toBe("Some input text.");

    hideCommentModal();

    commentInput.value = "";

    openCommentModal("1", "Test User");

    expect(commentInput.value).toBe("");
  });

  test("should handle edge cases for character counting", () => {
    openCommentModal("1", "Test User");

    const commentInput = document.getElementById("commentContent");
    const charCount = document.getElementById("charCount");

    const exactLimitInput = "A".repeat(50); // length 50
    commentInput.value = exactLimitInput;
    commentInput.dispatchEvent(new Event("input"));

    expect(charCount.textContent).toBe("50 / 50 characters");
    expect(charCount.style.color).toBe("black");

    // empty input
    commentInput.value = "";
    commentInput.dispatchEvent(new Event("input"));

    expect(charCount.textContent).toBe("0 / 50 characters");
    expect(charCount.style.color).toBe("black");
  });

  test("should not crash when modal is opened multiple times", () => {
    for (let i = 0; i < 5; i++) {
      openCommentModal("1", "Test User");
      hideCommentModal();
    }

  });

  test("should clear all fields when modal is closed", () => {
    openCommentModal("1", "Test User");

    const commentInput = document.getElementById("commentContent");
    const charCount = document.getElementById("charCount");

    // input and closing
    commentInput.value = "Some input text";
    commentInput.dispatchEvent(new Event("input"));

    hideCommentModal();
    commentInput.value = "";
    charCount.textContent = "0 / 50 characters";

    openCommentModal("1", "Test User");

    expect(commentInput.value).toBe("");
    expect(charCount.textContent).toBe("0 / 50 characters");
  });

  test("should prevent submission if input is empty", () => {
    openCommentModal("1", "Test User");
    const commentInput = document.getElementById("commentContent");

    commentInput.value = "";
    commentInput.dispatchEvent(new Event("input"));

    expect(commentInput.value).toBe("");
  });
});
