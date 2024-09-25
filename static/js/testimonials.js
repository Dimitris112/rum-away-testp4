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

  // Modal Functions
  function openCommentModal(testimonialId, userName) {
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

    const commentModal = new bootstrap.Modal(
      document.getElementById("commentModal")
    );
    commentModal.show();
  }

  function openEditCommentModal(commentId, commentContent) {
    document.getElementById("editCommentId").value = commentId;
    document.getElementById("editCommentContent").value = commentContent;

    const editCommentInput = document.getElementById("editCommentContent");
    const editCharCount = document.getElementById("editCharCount");
    editCharCount.textContent = "0 / 50 characters";

    editCommentInput.addEventListener("input", () => {
      const currentLength = editCommentInput.value.length;
      editCharCount.textContent = `${currentLength} / 50 characters`;
      editCharCount.style.color = currentLength > 50 ? "red" : "black";
    });

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

  function openUserInfoModal(userId, userName) {
    fetch(`/api/v1/users/${userId}/profile/`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        document.getElementById("userProfilePicture").src =
          data.profile_picture;
        document.getElementById("userName").textContent = data.username;
        document.getElementById(
          "memberSince"
        ).textContent = `Member Since: ${data.member_since}`;
        document.getElementById("userBio").textContent = data.bio;
        document.getElementById(
          "userInfoModalLabel"
        ).textContent = `${data.username} Info`;

        const userInfoModal = new bootstrap.Modal(
          document.getElementById("userInfoModal")
        );
        userInfoModal.show();
      })
      .catch((error) => {
        console.error("Error fetching user info:", error);
      });
  }

  // Event Listeners
  document.querySelectorAll(".user-profile-link").forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const userId = link.getAttribute("data-user-id");
      const userName = link.getAttribute("data-user-name");
      openUserInfoModal(userId, userName);
    });
  });

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
        console.error("An error occurred while adding your comment:", error);
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
            const commentParagraph = commentElement.querySelector("p");
            commentParagraph.textContent = commentContent;

            const editedText = document.createElement("span");
            editedText.textContent = " (Edited)";
            editedText.style.color = "rgba(33, 37, 41, 0.75)";
            editedText.style.fontSize = "14px";

            const existingEditedText =
              commentElement.querySelector(".edited-text");
            if (existingEditedText) {
              existingEditedText.remove();
            }

            commentParagraph.appendChild(editedText);
            editedText.classList.add("edited-text");

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
          console.error("An error occurred while editing your comment:", error);
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
        console.error("An error occurred while deleting your comment:", error);
      });
  });

  // Sort testimonials
  function sortTestimonials(event) {
    event.preventDefault();

    const sortValue = document
      .querySelector(".custom-select .selected")
      .getAttribute("data-value");
    const sortOrder = document.querySelector(
      'input[name="sortOrder"]:checked'
    ).value; // Ascending or Descending
    window.history.replaceState(
      null,
      "",
      "?sort=" + sortValue + "&order=" + sortOrder
    );

    const testimonialList = document.querySelector(
      ".testimonial-container .row"
    );
    const testimonials = Array.from(testimonialList.children);

    const sortedTestimonials = sortByCriteria(
      testimonials,
      sortValue,
      sortOrder
    );

    // Clear the current list and append sorted testimonials
    testimonialList.innerHTML = "";
    sortedTestimonials.forEach((testimonial) => {
      testimonialList.appendChild(testimonial);
    });
  }

  function getValue(testimonial, sortValue) {
    switch (sortValue) {
      case "views":
        return parseInt(testimonial.getAttribute("data-views"), 10);
      case "comments":
        return parseInt(testimonial.getAttribute("data-comments"), 10);
      case "rating":
        return parseFloat(testimonial.getAttribute("data-rating"));
      case "date":
      default:
        return new Date(testimonial.getAttribute("data-date")).getTime();
    }
  }

  function sortByCriteria(testimonials, sortValue, sortOrder) {
    return testimonials.sort((a, b) => {
      let aValue = getValue(a, sortValue);
      let bValue = getValue(b, sortValue);

      return sortOrder === "asc" ? aValue - bValue : bValue - aValue;
    });
  }

  // Event listener for sorting options
  document.querySelectorAll(".option").forEach((option) => {
    option.addEventListener("click", function () {
      const selected = document.querySelector(".custom-select .selected");
      selected.setAttribute("data-value", this.getAttribute("data-value"));
      selected.querySelector("#selectedOption").textContent = this.textContent;
      sortTestimonials(event);
    });
  });

  document.querySelectorAll('input[name="sortOrder"]').forEach((input) => {
    input.addEventListener("change", sortTestimonials);
  });

  function loadMoreTestimonials(event) {
    event.preventDefault();

    const loadMoreButton = document.querySelector(".load-more-button");
    const offset = parseInt(loadMoreButton.getAttribute("data-offset"));
    const sort = document.querySelector("#sortOptions").value;
    const testimonialsContainer = document.querySelector(
      ".testimonial-container .row"
    );

    loadMoreButton.textContent = "Loading...";
    loadMoreButton.setAttribute("disabled", true);

    // AJAX to fetch more testimonials
    fetch(`/testimonials/?offset=${offset}&sort=${sort}`, {
      method: "GET",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        // Check if any testimonials returned
        if (data.testimonials.length > 0) {
          data.testimonials.forEach((testimonial) => {
            const testimonialCard = `
                <article class="col-md-6 mb-4 testimonial-card">
                  <div class="card shadow-sm">
                    <header class="card-header d-flex align-items-center">
                      <img src="${testimonial.profile_picture_url}" alt="${testimonial.name}'s profile picture" class="rounded-circle me-2" style="width: 50px; height: 50px;">
                      <h5 class="mb-0">${testimonial.name}</h5>
                    </header>
                    <div class="card-body">
                      <p class="text-muted">${testimonial.content}</p>
                      <div class="d-flex justify-content-between mt-2">
                        <span class="text-muted">${testimonial.views_count} <strong>views</strong></span>
                        <span class="text-muted">${testimonial.comments_count} <strong>comments</strong></span>
                      </div>
                      <small class="text-muted">Submitted on: ${testimonial.created_at}</small>
                    </div>
                  </div>
                </article>
              `;
            testimonialsContainer.insertAdjacentHTML(
              "beforeend",
              testimonialCard
            );
          });

          loadMoreButton.setAttribute(
            "data-offset",
            offset + data.testimonials.length
          ); // Offset +4 8 12 ...

          if (data.total_count <= offset + data.testimonials.length) {
            loadMoreButton.style.display = "none";
          }
        } else {
          loadMoreButton.style.display = "none";
        }
      })
      .catch((error) => {
        console.error("Error loading testimonials:", error);
        alert("Failed to load testimonials. Please try again later.");
      })
      .finally(() => {
        // Reset loading state
        loadMoreButton.textContent = "Load More Testimonials";
        loadMoreButton.removeAttribute("disabled");
      });
  }

  document
    .querySelector(".load-more-button")
    .addEventListener("click", loadMoreTestimonials);
});
