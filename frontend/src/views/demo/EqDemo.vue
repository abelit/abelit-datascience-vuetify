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
                  <canvas id="can" :width="tableWidth" height="100px" class="id1"></canvas>
                  <!-- <canvas id="can" :width="tableWidth" height="100px" v-else class="id2"></canvas> -->
                </div>

                <table border="1" cellspacing="0" cellpadding="0" ref="etable">
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
    selected: ["A", "B", "AB"],
    // canvasWidth: 1200 + "px",
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
    // tableWidth: {
    //   get: function() {
    //     // return this.$refs.etable.offsetWidth+"px";
    //     // console.log(this.$refs.etable.offsetWidth)
    //     return 1200+"px"
    //   }
    // }
  },
  methods: {
    restart() {
      this.currentYear = 10;
      this.step = 0;
      this.clearCanvas();
      this.drawLine(
        (this.$refs.etable.offsetWidth / this.topYear) * this.currentYear
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
        (this.$refs.etable.offsetWidth / this.topYear) * this.currentYear
      );

      this.clearCanvas();
      if (this.currentYear > 0) {
        this.drawLine(
          (this.$refs.etable.offsetWidth / this.topYear) * this.currentYear
        );
      }
    },
    drawLine(width) {
      //获取画板
      var can = document.getElementById("can");
      if (can == null) return false;
      var ctx = can.getContext("2d"); //得到画笔

      // //重绘画布内容
      // can.height = can.height;
      // console.log("height: " + can.height);

      ctx.beginPath(); //开始绘制新路径
      //画线
      arrow_line("can", 0, 90, 0, 0, width, 0); //横  （向右）
      // arrow_line("can",0,0,0,0,0,150);   //竖 (向下)
      arrow_line("can", 0, 0, 5, 0, 0, 0); //横  （向左）
      // arrow_line("can",150,-150,0,150,0,0);   //竖 (向上)
      //画带箭头的线
      function arrow_line(canId, ox, oy, x1, y1, x2, y2) {
        //参数说明 canvas的 id ，原点坐标  第一个端点的坐标，第二个端点的坐标
        var sta = new Array(x1, y1);
        var end = new Array(x2, y2);
        var canvas = document.getElementById(canId);
        if (canvas == null) return false;
        var ctx = canvas.getContext("2d");
        //画线
        ctx.beginPath();
        ctx.translate(ox, oy, 0); //坐标源点
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
          ctx.rotate(Math.PI - ang); //加个180度，反过来
        }
        ctx.lineTo(-5, -10);
        ctx.lineTo(0, -5);
        ctx.lineTo(5, -10);
        ctx.lineTo(0, 0);
        ctx.fill(); //箭头是个封闭图形
        ctx.restore(); //恢复到堆的上一个状态，其实这里没什么用。
        ctx.closePath();
      }
    },
    clearCanvas() {
      //获取画板
      var can = document.getElementById("can");
      if (can == null) return false;
      //清除画布内容
      can.height = can.height;
    }
  },
  mounted() {
    this.drawLine(this.$refs.etable.offsetWidth);
    // this.drawLine(0);
    this.tableWidth = this.$refs.etable.offsetWidth + "px";
  }
};
</script>