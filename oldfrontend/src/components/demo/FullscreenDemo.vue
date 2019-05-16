<template>
  <div id="app" >
    
    <div >
      <div class="example">
        <v-carousel>
          <v-carousel-item v-for="(item,i) in items" :key="i" :src="item.src"></v-carousel-item>
        </v-carousel>
      </div>
      <div>
        <v-container fluid>
          <v-sparkline
            :value="value"
            :gradient="gradient"
            :smooth="radius || false"
            :padding="padding"
            :line-width="width"
            :stroke-linecap="lineCap"
            :gradient-direction="gradientDirection"
            auto-draw
          ></v-sparkline>

          <v-divider></v-divider>

          <v-layout wrap>
            <v-flex xs12 md6>
              <v-layout fill-height align-center>
                <v-item-group v-model="gradient" mandatory>
                  <v-layout>
                    <v-item v-for="(gradient, i) in gradients" :key="i" :value="gradient">
                      <v-card
                        slot-scope="{ active, toggle }"
                        :style="{
                    background: gradient.length > 1
                      ? `linear-gradient(0deg, ${gradient})`
                      : gradient[0],
                    border: '2px solid',
                    borderColor: active ? '#222' : 'white'
                  }"
                        width="30"
                        height="30"
                        class="mr-2"
                        @click.native="toggle"
                      ></v-card>
                    </v-item>
                  </v-layout>
                </v-item-group>
              </v-layout>
            </v-flex>

            <v-flex xs12 md6>
              <v-slider v-model="width" label="Width" min="0.1" max="10" step="0.1" thumb-label></v-slider>
            </v-flex>

            <v-flex xs6>
              <v-layout fill-height align-center>
                <v-subheader class="pl-0">Linecap</v-subheader>
                <v-btn-toggle v-model="lineCap" mandatory>
                  <v-btn flat value="butt">butt</v-btn>
                  <v-btn flat value="round">round</v-btn>
                  <v-btn flat value="square">square</v-btn>
                </v-btn-toggle>
              </v-layout>

              <v-layout fill-height align-center>
                <v-subheader class="pl-0">Gradient direction</v-subheader>
                <v-btn-toggle v-model="gradientDirection" mandatory>
                  <v-btn flat value="top">top</v-btn>
                  <v-btn flat value="right">right</v-btn>
                  <v-btn flat value="left">left</v-btn>
                  <v-btn flat value="bottom">bottom</v-btn>
                </v-btn-toggle>
              </v-layout>
            </v-flex>

            <v-flex xs12 md6>
              <v-slider v-model="radius" label="Radius" min="0" max="25" thumb-label></v-slider>
            </v-flex>

            <v-flex xs12 md6 offset-md6>
              <v-slider v-model="padding" label="Padding" min="0" max="25" thumb-label></v-slider>
            </v-flex>
          </v-layout>
        </v-container>
      </div>
      <div>
        <v-stepper v-model="e1">
          <v-stepper-header>
            <v-stepper-step :complete="e1 > 1" step="1">Name of step 1</v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step :complete="e1 > 2" step="2">Name of step 2</v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step step="3">Name of step 3</v-stepper-step>
          </v-stepper-header>

          <v-stepper-items>
            <v-stepper-content step="1">
              <v-card class="mb-5" color="grey lighten-1" height="200px"></v-card>

              <v-btn color="primary" @click="e1 = 2">Continue</v-btn>

              <v-btn flat>Cancel</v-btn>
            </v-stepper-content>

            <v-stepper-content step="2">
              <v-card class="mb-5" color="grey lighten-1" height="200px"></v-card>

              <v-btn color="primary" @click="e1 = 3">Continue</v-btn>

              <v-btn flat>Cancel</v-btn>
            </v-stepper-content>

            <v-stepper-content step="3">
              <v-card class="mb-5" color="grey lighten-1" height="200px"></v-card>

              <v-btn color="primary" @click="e1 = 1">Continue</v-btn>

              <v-btn flat>Cancel</v-btn>
            </v-stepper-content>
          </v-stepper-items>
        </v-stepper>
      </div>
    </div>
    <div>
      <div id="example-3">
        <input type="checkbox" id="jack" value="Jack" v-model="checkedNames">
        <label for="jack">Jack</label>
        <input type="checkbox" id="john" value="John" v-model="checkedNames">
        <label for="john">John</label>
        <input type="checkbox" id="mike" value="Mike" v-model="checkedNames">
        <label for="mike">Mike</label>
        <br>
        <span>Checked names: {{ checkedNames }}</span>
      </div>
    </div>
    <div>
      <input type="radio" id="one" value="One" v-model="picked">
      <label for="one">One</label>
      <br>
      <input type="radio" id="two" value="Two" v-model="picked">
      <label for="two">Two</label>
      <br>
      <span>Picked: {{ picked }}</span>

      <input v-model="message" placeholder="edit me">
      <p>Message is: {{ message }}</p>
    </div>
    <div>
      <button v-on:mouseover="btnClick">点击此在后台控制台看到信息</button>
    </div>
    <button type="button" @click="toggle">Fullscreen</button>
  </div>
  
</template>
<script>
import fullscreen from "vue-fullscreen";
import Vue from "vue";
Vue.use(fullscreen);
const gradients = [
  ["#222"],
  ["#42b3f4"],
  ["red", "orange", "yellow"],
  ["purple", "violet"],
  ["#00c6ff", "#F0F", "#FF0"],
  ["#f72047", "#ffd200", "#1feaea"]
];
export default {
  methods: {
    toggle() {
      this.$fullscreen.toggle(this.$el.querySelector(".example"), {
        wrap: false,
        callback: this.fullscreenChange
      });
      console.log("fullscrenn o ooo");
    },
    fullscreenChange(fullscreen) {
      this.fullscreen = fullscreen;
    },
    btnClick() {
      console.log(this.message);
    }
  },
  data() {
    return {
      message: "",
      fullscreen: false,
      items: [
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg"
        },
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/sky.jpg"
        },
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/bird.jpg"
        },
        {
          src: "https://cdn.vuetifyjs.com/images/carousel/planet.jpg"
        }
      ],
      width: 2,
      radius: 10,
      padding: 8,
      lineCap: "round",
      gradient: gradients[5],
      value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
      gradientDirection: "top",
      gradients,
      e1: 0,
      checkedNames: [],
      picked: ""
    };
  }
};
</script>


<style lang="css" scoped>
#app {
  padding-top: 80px;
}
</style>