// Handles role change and delete modals for the Admin Users page

document.addEventListener("DOMContentLoaded", () => {
  const changeRoleModal = document.getElementById("changeRoleModal");
  const deleteUserModal = document.getElementById("deleteUserModal");

  if (changeRoleModal) {
    changeRoleModal.addEventListener("show.bs.modal", (event) => {
      const button = event.relatedTarget;
      const userId = button.getAttribute("data-user-id");
      const userName = button.getAttribute("data-user-name");
      const userRole = button.getAttribute("data-user-role");

      document.getElementById("changeRoleText").textContent =
        `Change role for ${userName}:`;

      const form = document.getElementById("changeRoleForm");
      form.action = `/admin/users/role/${userId}`;
      form.querySelector("select").value = userRole;
    });
  }

  if (deleteUserModal) {
    deleteUserModal.addEventListener("show.bs.modal", (event) => {
      const button = event.relatedTarget;
      const userId = button.getAttribute("data-user-id");
      const userName = button.getAttribute("data-user-name");

      document.getElementById("deleteUserText").textContent =
        `Are you sure you want to delete ${userName}?`;

      const form = document.getElementById("deleteUserForm");
      form.action = `/admin/users/delete/${userId}`;
    });
  }
});
