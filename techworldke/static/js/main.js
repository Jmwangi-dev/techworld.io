// static/js/main.js
document.addEventListener("DOMContentLoaded", function () {
  // Enhanced add to cart functionality with smooth transitions
  const addToCartButtons = document.querySelectorAll(".add-to-cart-button");

  addToCartButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const productId = button.getAttribute("data-product-id");
      addToCart(productId);
    });
  });

  function addToCart(productId) {
    // AJAX request for adding product to cart
    fetch(`/add_to_cart/${productId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response from the server
        alert(data.message);
        // You might want to update the cart UI dynamically
        // ...

        // Example: Reload the page to reflect changes
        location.reload();
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  // Enhanced remove from cart functionality with smooth transitions
  const removeFromCartButtons = document.querySelectorAll(
    ".remove-from-cart-button"
  );

  removeFromCartButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const cartItemId = button.getAttribute("data-cart-item-id");
      removeFromCart(cartItemId);
    });
  });

  function removeFromCart(cartItemId) {
    // AJAX request for removing product from cart
    fetch(`/remove_from_cart/${cartItemId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response from the server
        alert(data.message);
        // You might want to update the cart UI dynamically
        // ...

        // Example: Reload the page to reflect changes
        location.reload();
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  // Add more enhanced JavaScript functionality based on your requirements
});
