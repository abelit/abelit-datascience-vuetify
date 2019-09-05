<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>


<style>
/* 
Disable page scrollbar
*/
html {
  overflow-y: auto;
}
</style>
