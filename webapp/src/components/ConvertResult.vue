<template>
    <img alt="Image from Flask server" class="convphoto mb-2"/>
</template>

<script>
export default {
    name:"ConvertResult",
    data() {
        return {
            imageSrc: null
        };
    }
};
</script>
<style scoped>
.convphoto{
    max-width: 100%;
}
</style>