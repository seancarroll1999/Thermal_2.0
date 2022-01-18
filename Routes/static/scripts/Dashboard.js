var imageUpload = document.getElementById("customFile");
var textArea = document.getElementById("message-text-area");
var sendImageButton = document.getElementById("print-image");
var cancelImageButton = document.getElementById("cancel-image");
var imagePreview = document.getElementById("file-upload-image");
var imageUploadFooter = document.getElementById("photo-upload-footer");
var dangerAlert = document.getElementById("danger-alert");
var successAlert = document.getElementById("success-alert");
var warningAlert = document.getElementById("warning-alert");

imageUpload.addEventListener("change", (e) => {
    // get a reference to the file
    const file = e.target.files[0];
    console.log(file)
    var fileType = file.type.split("/")[0]
    if(fileType == "image"){
      dangerAlert.style.display = "none";
      // encode the file using the FileReader API
      const reader = new FileReader();
      reader.onloadend = () => {
        // use a regex to remove data url part
        var base64String = "";
        base64String = reader.result;
        imagePreview.setAttribute('src', base64String);
        imageUploadFooter.style.display = "block";
      };
      reader.readAsDataURL(file);
    } else {
      dangerAlert.textContent = "Error - Please select an image";
      dangerAlert.style.display = "block";
    }
  });

  textArea.addEventListener("keyup", ({key}) => {
    if(key == "Enter"){
      CheckTextAreaLines(textArea);
    }
  });

  textArea.addEventListener("change", (e) => {
    var lines = (textArea.value.match(/\n/g) || '').length + 1  
    var maxLines = textArea.rows;
    
    if(lines+1 < maxLines){
      textArea.rows = lines+1;
    }
  });

  function CheckTextAreaLines(textarea){
    var lines = (textarea.value.match(/\n/g) || '').length + 1  
    var maxLines = textarea.rows;
    if(lines >= maxLines){
      textarea.rows++;
    }
  }

  sendImageButton.addEventListener("click", (e) => {
    sendImageButton.disabled = true;
    var base64String = imagePreview.src
        .replace("data:", "")
        .replace(/^.+,/, "");
      
      if (base64String != "")
      {
        var formData = new FormData();
        formData.append("img", base64String);
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function()
        {
            if(xmlHttp.readyState == 4 && xmlHttp.status == 200)
            {
                if(xmlHttp.responseText == "Done"){
                  successAlert.textContent = "Success - Image printing";
                  successAlert.style.display = "block";
                } else if(xmlHttp.responseText == "Busy")
                {
                  warningAlert.textContent = "Success - Image printing";
                  warningAlert.style.display = "block";
                }
            }
            sendImageButton.disabled = false;
        }
        xmlHttp.open("post", "/SendImage"); 
        xmlHttp.send(formData); 
      }
  });

  cancelImageButton.addEventListener("click", (e) => {
    successAlert.style.display = "none";
    dangerAlert.style.display = "none";
    removeImagePreview();
  });

  function removeImagePreview(){
    imagePreview.src = "";
  }