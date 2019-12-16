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
                <span class="display-1">当前步骤：{{step}}</span>
                <v-spacer></v-spacer>
                <span class="display-1">当前年： {{ currentYear }}</span>
              </v-col>
            </v-row>
            <v-row justify="center" align="center">
              <v-col>
                <div>
                  <canvas id="canvas" ref="canvas" :width="tableWidth" height="100px"></canvas>
                </div>
                <table border="1" cellspacing="0" cellpadding="0" ref="table">
                  <tr style="height: 50px">
                    <td
                      v-for="item in allContent"
                      :key="item"
                      style="width: 30px; text-align: center"
                      :style="item<=4*currentYear?'background-color: green;':''"
                    >{{item}}</td>
                  </tr>
                </table>
              </v-col>
            </v-row>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn class="primary" @click="change('A')">A</v-btn>
            <v-btn class="yellow darken-3" @click="change('AB')">A & B</v-btn>
            <v-btn class="purple" @click="change('B')">B</v-btn>
            <v-btn class="purple" v-if="step>0" @click="restart">
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
    currentYear: 10,
    topYear: 10,
    step: 0,
    selected: [],
    tableWidth: "1129px"
  }),
  computed: {
    allContent: {
      get: function() {
        var arr = [];
        for (var i = 1; i <= 4 * this.topYear; i++) {
          arr.push(i);
        }
        return arr;
      }
    }
  },
  methods: {
    restart() {
      this.currentYear = 10;
      this.step = 0;
      this.clearCanvas();
      this.drawLine(
        (this.$refs.table.offsetWidth / this.topYear) * this.currentYear
      );
    },
    change(type) {
      if (type === "A") {
        if (this.currentYear === 0) {
          alert("Next Question about B.");
          return;
        } else if (
          (this.currentYear <= 1 && this.currentYear > 0) ||
          (this.currentYear > 9 && this.currentYear <= 10)
        ) {
          if (this.currentYear === 10 && this.step === 0) {
            this.currentYear = this.currentYear - 10;
          } else {
            this.currentYear = this.currentYear - 0.5;
          }
        } else if (this.currentYear > 1 && this.currentYear <= 9) {
          if (
            this.step > 2 &&
            this.selected[this.selected.length - 1] != type
          ) {
            this.currentYear = this.currentYear - 0.5;
          } else {
            if (this.currentYear % 1 === 0.5) {
              this.currentYear = this.currentYear - 0.5;
            } else {
              this.currentYear = this.currentYear - 1;
            }
          }
        } else {
          alert("Warning ...");
        }
      } else if (type === "B") {
        if (this.currentYear === 0) {
          if (this.step === 1) {
            this.currentYear = this.currentYear + 5;
          } else {
            this.currentYear = this.currentYear + 0.5;
          }
        } else if (
          (this.currentYear < 1 && this.currentYear > 0) ||
          (this.currentYear >= 9 && this.currentYear < 10)
        ) {
          this.currentYear = this.currentYear + 0.5;
        } else if (this.currentYear >= 1 && this.currentYear <= 9) {
          if (
            this.step > 2 &&
            this.selected[this.selected.length - 1] != type
          ) {
            this.currentYear = this.currentYear + 0.5;
          } else {
            if (this.currentYear % 1 === 0.5) {
              this.currentYear = this.currentYear + 0.5;
            } else {
              this.currentYear = this.currentYear + 1;
            }
          }
        } else {
          alert("Warning ...");
          return;
        }
      } else {
        alert("A & B");
        return;
      }
      this.selected.push(type);
      this.step++;
      console.log(
        (this.$refs.table.offsetWidth / this.topYear) * this.currentYear
      );

      this.clearCanvas();
      if (this.currentYear > 0) {
        this.drawLine(
          (this.$refs.table.offsetWidth / this.topYear) * this.currentYear
        );
      }
    },
    drawLine(width) {
      //获取画板
      var canvas = document.getElementById("canvas");
      if (canvas == null) return false;
      //获取画笔
      var ctx = canvas.getContext("2d");
      //开始绘制新路径
      ctx.beginPath();
      //画线
      //横  （向右）
      drawArrowLine("canvas", 0, 90, 0, 0, width, 0);
      //横  （向左）
      drawArrowLine("canvas", 0, 0, 5, 0, 0, 0);
      canvas;
      //画带箭头的线
      function drawArrowLine(canId, ox, oy, x1, y1, x2, y2) {
        //参数说明 canvas的 id ，原点坐标  第一个端点的坐标，第二个端点的坐标
        var sta = new Array(x1, y1);
        var end = new Array(x2, y2);
        var canvas = document.getElementById(canId);
        if (canvas == null) return false;
        var ctx = canvas.getContext("2d");
        //画线
        ctx.beginPath();
        //坐标源点
        ctx.translate(ox, oy, 0);
        ctx.moveTo(sta[0], sta[1]);
        ctx.lineTo(end[0], end[1]);
        ctx.fill();
        ctx.stroke();
        ctx.save();
        //画箭头
        ctx.translate(end[0], end[1]);
        //我的箭头本垂直向下，算出直线偏离Y的角，然后旋转 ,rotate是顺时针旋转的，所以加个负号
        var ang = (end[0] - sta[0]) / (end[1] - sta[1]);
        ang = Math.atan(ang);
        if (end[1] - sta[1] >= 0) {
          ctx.rotate(-ang);
        } else {
          // 旋转180度
          ctx.rotate(Math.PI - ang);
        }
        ctx.lineTo(-5, -10);
        ctx.lineTo(0, -5);
        ctx.lineTo(5, -10);
        ctx.lineTo(0, 0);
        ctx.fill();
        ctx.restore();
        ctx.closePath();
      }
    },
    clearCanvas() {
      //获取画板
      var canvas = document.getElementById("canvas");
      if (canvas == null) return false;
      //清除画布内容
      canvas.height = canvas.height;
    }
  },
  mounted() {
    this.drawLine(this.$refs.table.offsetWidth);
    // this.drawLine(0);
    this.tableWidth = this.$refs.table.offsetWidth + "px";

    console.log(document.getElementById("canvas"));
    console.log(this.$refs.canvas);
  }
};
</script>