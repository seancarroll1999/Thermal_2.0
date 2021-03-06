var imageUpload = document.getElementById("customFile");
var textArea = document.getElementById("message-text-area");
var sendImageButton = document.getElementById("print-image");
var cancelImageButton = document.getElementById("cancel-image");
var imagePreview = document.getElementById("file-upload-image");
var imageUploadFooter = document.getElementById("photo-upload-footer");
var dangerAlert = document.getElementById("danger-alert");
var successAlert = document.getElementById("success-alert");
var warningAlert = document.getElementById("warning-alert");
var sendMessageButton = document.getElementById("print-message");

var textAreaMinLines = 5

//Feature Buttons
var morningMessageBtn = document.getElementById("morningMessageBtn");
var googleCalendarBtn = document.getElementById("googleCalendarBtn");
var cryptoBtn = document.getElementById("cryptoBtn");
var sudokuBtn = document.getElementById("sudokuBtn");
var sudokuPrintBtn = document.getElementById("sudokuPrintBtn");
var quoteBtn = document.getElementById("quoteBtn");

var featureList = {
  'printMorningMessage' : morningMessageBtn,
  'printCrypto' : cryptoBtn,
  'printGoogleCalendar' : googleCalendarBtn,
  'printSudoku' : sudokuBtn,
  'printSudokuAnswer' : sudokuPrintBtn,
  'printQuote' : quoteBtn
};


for(let featureValue in featureList){
  featureList[featureValue].addEventListener("click", (e) => {
    var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function()
        {
            if(xmlHttp.readyState == 4 && xmlHttp.status == 200)
            {
              successAlert.textContent = `Success - Printed ${xmlHttp.responseText}`;
              successAlert.style.display = "block";
              successAlert.scrollIntoView();
            }
        }
        xmlHttp.open("get", `/API/v1/webKey/${featureValue}`, true); 
        xmlHttp.send(); 
  });
}



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
      dangerAlert.scrollIntoView()
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
    
    if(lines+1 < maxLines && lines+1 > textAreaMinLines){
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
                  successAlert.scrollIntoView()
                  clearImage()
                }
            }
        }
        xmlHttp.open("post", "/SendImage"); 
        xmlHttp.send(formData); 
      }
  });

  cancelImageButton.addEventListener("click", (e) => {
    successAlert.style.display = "none";
    dangerAlert.style.display = "none";
    clearImage();
  });

  function clearImage(){
    imageUpload.value = ''
    imagePreview.src = "";
  }

  sendMessageButton.addEventListener("click", (e) => {
    if(textArea.value != ""){
        var formData = new FormData();
        formData.append("msg", textArea.value);
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function()
        {
            if(xmlHttp.readyState == 4 && xmlHttp.status == 200)
            {
                if(xmlHttp.responseText == "Done"){
                  successAlert.textContent = "Success - Message sent";
                  successAlert.style.display = "block";
                  textArea.value = '';
                  successAlert.scrollIntoView();
                }
            }
        }
        xmlHttp.open("post", "/SendMessage"); 
        xmlHttp.send(formData); 
    }
  });