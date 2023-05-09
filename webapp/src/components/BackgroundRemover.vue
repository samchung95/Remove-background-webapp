<template>
  <div class="row m-3 mx-2">
    <div class="col-lg-6">
      <div class="container d-flex main border-5 border-primary" :class="{ 'dragging': dragging }"
        @dragover.prevent="onDragEnter" @dragenter.prevent="onDragEnter" @dragleave.prevent="onDragLeave"
        @drop.prevent="onDrop" @paste="handlePaste">

        <span class="my-auto mx-auto">
          <h2 class="text-center">Drop your photos here or <br> simply paste your photo to start converting!</h2>
          <input type="file" ref="imageUpload" multiple @change="handleImageUpload" style="display:none" />
          <button type="button" @click="uploadImages" class="btn btn-primary mt-2">Convert now</button>
        </span>


      </div>
    </div>
    <div class="col-lg-6">
      <span>
        <h4>Files converted</h4>
      </span>
      <br>
      <div class="col">
        <ConvertResult 
        v-for="(obj, index) in converted_photos" 
        :key="index" 
        :src="obj.url" />
      </div>
    </div>
  </div>
</template>
  
<script>

import ConvertResult from "./ConvertResult.vue"

export default {
  name: 'BackgroundRemover',
  components: {
    ConvertResult
  },
  data() {
    return {
      dragging: false,
      imageUrl: "",
      imageSrc: "",
      converted_photos:[

      ]
    };
  },
  methods: {
    onDragEnter() {
      this.dragging = true;
    },

    onDragLeave() {
      this.dragging = false;
    },
    onDrop(event) {
      // Get the files from the event dataTransfer object
      const files = event.dataTransfer.files;

      // Loop through the files and handle each one
      for (let i = 0; i < files.length; i++) {
        const file = files[i];

        // Check if the file is an image
        if (file.type.startsWith("image/")) {
          this.handleImageFile(file);
        } else {
          console.log("Not an image file:", file.name);
        }
      }
    },
    async handleImageFile(file) {
      // Handle the dropped image file here
      console.log("Image file:", file.name);

      // Example: Read the image file as a data URL
      const reader = new FileReader();
      const formData = new FormData();
      formData.append('image', file);
      try {
        const response = await fetch('http://localhost:5001/upload', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          const blob = await response.blob();
          console.log('Success:', blob);
          let len = this.converted_photos.length
          let imageSrc = URL.createObjectURL(blob);
          this.converted_photos.push({
            "name":"image"+ String(len)+".png",
            "url":imageSrc
          })
          
        } else {
          console.error('Failed to fetch image from server');
        }

      } catch (error) {
        console.error('Error:', error);
      }

      reader.onload = (event) => {
        console.log("Image data URL:", event.target.result);
      };
      reader.readAsDataURL(file);
    },
    uploadImages() {
      this.$refs.imageUpload.click();
    },

    handleImageUpload(event) {
      const files = event.target.files;

      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        this.handleImageFile(file)
        if (file.type.startsWith("image/")) {
          console.log("Image file:", file);
        } else {
          console.log("Not an image file:", file);
        }
      }
    },
    async processImageBlob(blob) {
      const file = new File([blob], 'image.jpg', { type: 'image/jpeg' })
      this.handleImageFile(file)
      // Process the image blob here
      console.log("Image blob:", blob);
    },
    async handlePaste(event) {
      event.preventDefault();

      const items = (event.clipboardData || event.originalEvent.clipboardData).items;

      for (const item of items) {
        if (item.type.indexOf("image") !== -1) {
          const blob = item.getAsFile();
          const reader = new FileReader();
          reader.onload = (e) => {
            this.imageUrl = e.target.result;
          };
          reader.readAsDataURL(blob);
          this.processImageBlob(blob); // Pass the image blob to the processImageBlob method
          return;
        } else if (item.type === "text/plain") {
          item.getAsString((text) => {
            if (this.isValidImageUrl(text)) {
              this.imageUrl = text;

              // Download the image, convert it to a blob, and pass it to the processImageBlob method
              fetch(text, {
                method: 'GET',
                mode: 'no-cors',
              })
                .then((response) => response.blob())
                .then((blob) => {
                  this.processImageBlob(blob);
                })
                .catch((error) => {
                  console.error("Failed to fetch image:", error);
                });

              return;
            }
          })

        }
      }
    },

    isValidImageUrl(url) {
      return url.match(/\.(jpeg|jpg|gif|png)$/) != null;
    },
  },
}
</script>
  
<style scoped>
.main {
  min-height: 80vh;
  /* min-width: 100%; */
  border-style: dashed;
}

.dragging {
  background-color: #f0f0f0;
}
</style>