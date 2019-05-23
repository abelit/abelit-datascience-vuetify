<template>
  <div v-if="!isProgressCircular">
    <v-tooltip bottom>
      <template v-slot:activator="{ on }">
        <v-btn color="primary" flat icon v-on="on" @click="cMethod">
          <v-icon>refresh</v-icon>
        </v-btn>
      </template>
      <span>{{$t("button.refresh")}}</span>
    </v-tooltip>
  </div>
  <div v-else>
    <v-progress-circular indeterminate color="primary"></v-progress-circular>
  </div>
</template>

<script>
export default {
  data: () => ({
    isProgressCircular: false
  }),
  props: {
    pMethod: {
      type: Function,
      default: null
    }
  },
  methods: {
    cMethod() {
      if (this.pMethod) {
        this.isProgressCircular = true;
        setTimeout(() => {
          this.isProgressCircular = false;
          this.pMethod();
        }, 2000);
      }
    }
  }
};
</script>
