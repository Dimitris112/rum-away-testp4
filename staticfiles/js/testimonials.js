document.addEventListener("DOMContentLoaded", () => {
  // Retrieve the CSRF token from cookies
  function getCookie(name) {
    const cookies = document.cookie.split(";").map((cookie) => cookie.trim());
    for (const cookie of cookies) {
      if (cookie.startsWith(`${name}=`)) {
        return decodeURIComponent(cookie.substring(name.length + 1));
      }
    }
    return null;
  }

  // Opens comment modal
  function openCommentModal(testimonialId, userName) {
    document.getElementById("testimonialId").value = testimonialId;
    document.getElementById("testimonialUserName").textContent = userName;

    const commentModal = new bootstrap.Modal(
      document.getElementById("commentModal")
    );
    commentModal.show();
  }

  // Opens edit comment modal
  function openEditCommentModal(commentId, commentContent) {
    document.getElementById("editCommentId").value = commentId;
    document.getElementById("editCommentContent").value = commentContent;

    const editCommentModal = new bootstrap.Modal(
      document.getElementById("editCommentModal")
    );
    editCommentModal.show();
  }

  function openDeleteConfirmModal(commentId) {
    document
      .getElementById("confirmDelete")
      .setAttribute("data-comment-id", commentId);
    const deleteModal = new bootstrap.Modal(
      document.getElementById("deleteCommentModal")
    );
    deleteModal.show();
  }

  document.querySelectorAll(".comment-button").forEach((button) => {
    button.addEventListener("click", () => {
      const testimonialId = button.getAttribute("data-testimonial-id");
      const userName = button.getAttribute("data-user-name");
      openCommentModal(testimonialId, userName);
    });
  });

  document.querySelectorAll(".edit-comment-button").forEach((button) => {
    button.addEventListener("click", () => {
      const commentId = button.getAttribute("data-comment-id");
      const commentContent = button.getAttribute("data-comment-content");
      openEditCommentModal(commentId, commentContent);
    });
  });

  // Add comment
  document.getElementById("commentForm").addEventListener("submit", (event) => {
    event.preventDefault();
    const testimonialId = document.getElementById("testimonialId").value;
    const commentContent = document.getElementById("commentContent").value;

    fetch(`/testimonials/${testimonialId}/add-comment/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify({ content: commentContent }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        if (data.success) {
          const commentSection = document.querySelector(
            `.comment-section[data-testimonial-id="${testimonialId}"]`
          );
          const newCommentHTML = `
                <div class="mt-2" data-comment-id="${data.comment_id}">
                  <strong>${data.user_name}</strong>:
                  <p>${commentContent}</p>
                  <small class="text-muted">${data.created_at}</small>
                  <div>
                    <button class="btn btn-warning btn-sm me-2 edit-comment-button" data-comment-id="${data.comment_id}" data-comment-content="${commentContent}">
                      Edit
                    </button>
                    <button class="btn btn-danger btn-sm delete-comment-button" data-comment-id="${data.comment_id}">
                      Delete
                    </button>
                  </div>
                </div>`;
          commentSection.insertAdjacentHTML("beforeend", newCommentHTML);

          const commentModal = bootstrap.Modal.getInstance(
            document.getElementById("commentModal")
          );
          commentModal.hide();
          document.getElementById("commentForm").reset();
        } else {
          console.error(
            data.error || "Failed to add comment. Please try again."
          );
        }
      })
      .catch((error) => {
        console.error(
          "An error occurred while adding your comment. Please try again."
        );
      });
  });

  // Edit comment
  document
    .getElementById("editCommentForm")
    .addEventListener("submit", (event) => {
      event.preventDefault();
      const commentId = document.getElementById("editCommentId").value;
      const commentContent =
        document.getElementById("editCommentContent").value;

      fetch(`/testimonials/comment/edit/${commentId}/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({ content: commentContent }),
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          if (data.success) {
            const commentSection = document.querySelector(
              `.comment-section[data-testimonial-id="${data.testimonial_id}"]`
            );
            const commentElement = commentSection
              .querySelector(`[data-comment-id="${commentId}"]`)
              .closest(".mt-2");
            commentElement.querySelector("p").textContent = commentContent;

            const editCommentModal = bootstrap.Modal.getInstance(
              document.getElementById("editCommentModal")
            );
            editCommentModal.hide();
            document.getElementById("editCommentForm").reset();
          } else {
            console.error(
              data.error || "Failed to edit comment. Please try again."
            );
          }
        })
        .catch((error) => {
          console.error(
            "An error occurred while editing your comment. Please try again."
          );
        });
    });

  // Delete comment
  document.addEventListener("click", (event) => {
    if (event.target.classList.contains("delete-comment-button")) {
      const commentId = event.target.getAttribute("data-comment-id");
      openDeleteConfirmModal(commentId);
    }
  });

  // Confirm deletion of the comment
  document.getElementById("confirmDelete").addEventListener("click", () => {
    const commentId = document
      .getElementById("confirmDelete")
      .getAttribute("data-comment-id");
    const commentElement = document.querySelector(
      `[data-comment-id="${commentId}"]`
    );

    fetch(`/testimonials/comment/delete/${commentId}/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        if (data.success) {
          commentElement.remove();
          const deleteModal = bootstrap.Modal.getInstance(
            document.getElementById("deleteCommentModal")
          );
          deleteModal.hide();
        } else {
          console.error(
            data.error || "Failed to delete comment. Please try again."
          );
        }
      })
      .catch((error) => {
        console.error(
          "An error occurred while deleting your comment. Please try again."
        );
      });
  });
});
