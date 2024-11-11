<template>
    <div class="about">
        <h1>This is page about</h1>
        <div class="content-about">test content about</div>
    </div>
</template>
  
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
    name: "About",
});
</script>
  
<style scoped lang="scss">
@import "@/styles/about.scss";

.about {
    // styles here
    color: red;
}
</style>