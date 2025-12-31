function submitImage() {
  const fileInput = document.getElementById("imageInput");
  const loader = document.getElementById("loader");

  if (!fileInput.files.length) {
    alert("Please select an image");
    return;
  }

  loader.classList.remove("hidden");

  const formData = new FormData();
  formData.append("image", fileInput.files[0]);

  fetch("http://127.0.0.1:5000/analyze", {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      localStorage.setItem("result", JSON.stringify(data));
      window.location.href = "result.html";
    })
    .catch(err => {
      alert("Error connecting to backend");
      console.error(err);
    });
}
