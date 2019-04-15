<template>
  <section class="app-main">
    <transition name="fade" mode="out-in">
      <keep-alive :include="cachedViews">
        <v-content id="content">
          <router-view :key="key"></router-view>
        </v-content>
      </keep-alive>
    </transition>
  </section>
</template>

<script>
export default {
  name: "AppMain"
};
</script>
