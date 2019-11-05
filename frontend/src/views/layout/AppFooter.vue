<template>
  <v-footer app :inset="inset" class="font-weight-medium" color="primary lighten-1">
    <v-col class="text-center" cols="12">
      &copy; {{ new Date().getFullYear() }} &nbsp; — &nbsp;
      <strong>Data Visualization & Analyzation</strong>
    </v-col>
  </v-footer>
</template>

<script>
export default {
  data: () => ({
    inset: true
  })
}
</script>