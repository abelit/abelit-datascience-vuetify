<template>
  <div class="">
    <vue-datepicker-local v-model="time" />
  </div>
</template>

<script>
import VueDatepickerLocal from 'vue-datepicker-local'

export default {
  components: {
    VueDatepickerLocal
  },
  data () {
    return {
      time: new Date()
    }
  }
}
</script>
