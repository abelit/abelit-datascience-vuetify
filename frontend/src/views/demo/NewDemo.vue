<template>
  <v-container class="grey lighten-5">
    <v-row justify="center" align="center">
      <v-col>
        <v-card justify="center" align="center">
          <v-card-title>Demo EQ Test</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-row>
              <v-col>
                <span class="display-1">步骤：{{step}}</span>
                <v-spacer></v-spacer>
                <span class="display-1">当前年： {{ currentYear/4 }}</span>
              </v-col>
            </v-row>
            <v-row justify="center" align="center">
              <v-col>
                 <table border="1" cellspacing="0" cellpadding="0">
                  <tr style="height: 50px">
                    <td  v-for="item in allYear" :key="item"  style="width: 30px; text-align: center" :style="item<=4*currentYear?'background-color: green;':''">{{item}}</td>
                  </tr>
                </table>
              </v-col>
            </v-row>

          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn class="primary" @click="change(0)">A</v-btn>
            <v-btn class="yellow darken-3" @click="change(-1)">A & B</v-btn>
            <v-btn class="purple" @click="change(1)">B</v-btn>
            <v-btn class="purple" @click="restart">
              <v-icon>refresh</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    currentYear: 40,
    topYear: 40,
    step: 1,
    width: 50,
    height: 50,
    elevation: 4,
    colors: ["white", "gray darken-2", "warning", "error", "success", "teal"],
    color: "blue",
    tile: false
  }),
  computed: {
    allYear: {
      get: function() {
        var arr = [];
        for (var i = 1; i <= this.topYear; i++) {
          arr.push(i);
        }
        return arr;
      }
    }
  },
  methods: {
    restart() {
      this.currentYear = 10;
      this.step = 1;
    },
    change(type) {
      if (type == 0) {
        if (this.step == 1) {
          this.currentYear = this.currentYear - 10;
        } else if (this.step == 2) {
          this.currentYear = this.currentYear - 5;
        } else if (this.step >= 3 && this.step < 7) {
          if (
            (this.currentYear <= 5 && this.currentYear > 1) ||
            (this.currentYear <= -5 && this.currentYear > -9)
          ) {
            this.currentYear = this.currentYear - 1;
          } else {
            this.currentYear = this.currentYear - 0.5;
          }
        } else if (this.step >= 7 && this.step <= 8) {
          this.currentYear = this.currentYear - 0.5;
        } else {
          alert("End ...");
          return;
        }
      } else if (type == 1) {
        if (this.step == 1) {
          alert("Nothing to do ...");
          return;
        } else if (this.step == 2) {
          this.currentYear = this.currentYear + 5;
        } else if (this.step >= 3 && this.step < 7) {
          if (
            (this.currentYear <= 5 && this.currentYear > 1) ||
            (this.currentYear <= -5 && this.currentYear > -9)
          ) {
            this.currentYear = this.currentYear + 0.5;
          } else {
            this.currentYear = this.currentYear + 1;
          }
        } else if (this.step >= 7 && this.step <= 8) {
          this.currentYear = this.currentYear + 0.5;
        } else {
          alert("End ...");
          return;
        }
      } else {
        alert("A & B");
        return;
      }
      this.step++;
    }
  }
};
</script>