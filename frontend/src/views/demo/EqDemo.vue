<template>
  <v-container class="grey lighten-5">
    <v-row justify="center" align="center">
      <v-col>
        <v-card justify="center" align="center">
          <v-card-title>Demo EQ Test</v-card-title>
          <v-divider></v-divider>
          <v-card-text v-if="slide === 1">
            <v-row>
              <v-col>
                <span class="display-1">当前SLIDE： {{ slide }}</span>
                <v-spacer></v-spacer>
                <span class="display-1">当前Direction： {{ stepDirection }}</span>
                <v-spacer></v-spacer>
                <span class="display-1">当前步骤：{{step}}</span>
                <v-spacer></v-spacer>
                <span class="display-1">当前步骤B：{{stepB}}</span>
                <v-spacer></v-spacer>
                <span class="display-1">当前年A： {{ currentYear }}</span>
                <v-spacer>
                  <span class="display-1">当前年B： {{ currentYearB }}</span>
                </v-spacer>
              </v-col>
            </v-row>
            <v-row justify="center" align="center">
              <v-col>
                <div>
                  <canvas id="canvas1" ref="canvas1" height="100px"></canvas>
                </div>
                <table border="1" cellspacing="0" cellpadding="0" ref="table1">
                  <tr style="height: 50px">
                    <td
                      v-for="item in allContent(topYear)"
                      :key="item"
                      style="text-align: center; width: 24px"
                      :class="item<=4*currentYear?'light-green lighten-1':''"
                    >{{item}}</td>
                  </tr>
                </table>
              </v-col>
            </v-row>
            <v-row justify="center" align="center" class="pt-12 mt-12">
              <v-col>
                <table border="1" cellspacing="0" cellpadding="0" ref="table2">
                  <tr style="height: 50px">
                    <td
                      v-for="item in allContent(topYear)"
                      :key="item"
                      style="text-align: center; width: 24px"
                      class="blue lighten-2"
                    >{{item}}</td>
                  </tr>
                </table>
                <div>
                  <canvas id="canvas2" ref="canvas2" height="100px"></canvas>
                </div>
              </v-col>
            </v-row>
          </v-card-text>

          <v-card-text v-if="slide === 2">
            <v-row>
              <v-col>
                <v-spacer></v-spacer>
                <span class="display-1">当前SLIDE： {{ slide }}</span>
                <v-spacer></v-spacer>
                <span class="display-1">当前Direction： {{ stepDirection }}</span>
                <v-spacer></v-spacer>
                <span class="display-1">当前步骤：{{step}}</span>
                <v-spacer></v-spacer>
                <span class="display-1">当前步骤B：{{stepB}}</span>
                <v-spacer></v-spacer>
                <span class="display-1">当前年A： {{ currentYear }}</span>
                <v-spacer></v-spacer>
                <span class="display-1">当前年B： {{ currentYearB }}</span>
              </v-col>
            </v-row>
            <v-row justify="center" align="center">
              <v-col>
                <div>
                  <canvas id="canvas3" ref="canvas3" height="100px"></canvas>
                </div>
                <table border="1" cellspacing="0" cellpadding="0" ref="table3">
                  <tr style="height: 50px">
                    <td
                      v-for="item in allContent(topYearB)"
                      :key="item"
                      style="text-align: center; width: 16px"
                      :class="item<=4*currentYearB?'light-green lighten-1':''"
                    ></td>
                  </tr>
                </table>
              </v-col>
            </v-row>
            <v-row justify="center" align="center" class="pt-12 mt-12">
              <v-col>
                <table border="1" cellspacing="0" cellpadding="0" ref="table4">
                  <tr style="height: 50px">
                    <td
                      v-for="item in allContent(topYearB)"
                      :key="item"
                      style="text-align: center; width: 16px"
                      :class="item<=40?'light-green lighten-1':'blue lighten-2'"
                    ></td>
                  </tr>
                </table>
                <div>
                  <canvas id="canvas4" ref="canvas4" height="100px"></canvas>
                </div>
              </v-col>
            </v-row>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn class="primary" @click="chooseAnswer('A')">A</v-btn>
            <v-btn class="yellow darken-3" @click="chooseAnswer('AB')">A & B</v-btn>
            <v-btn class="purple" @click="chooseAnswer('B')">B</v-btn>
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
    currentYearB: 10,
    topYearB: 20,
    stepB: 0,
    selected: [],
    tableWidth: "",
    slide: 1,
    stepDirection: 0
  }),

  methods: {
    restart() {
      this.slide = 1;
      this.currentYear = 10;
      this.step = 0;
      this.currentYearB = 10;
      this.stepB = 0;
      this.stepDirection = 0;

      this.$nextTick(() => {
        if (this.slide === 1) {
          this.clearCanvas("canvas1");
          this.drawLine(
            (this.$refs.table1.offsetWidth / this.topYear) * this.currentYear,
            "canvas1",
            90,0
          );
        }
        if (this.slide === 2) {
          this.clearCanvas("canvas3");
          // this.clearCanvas("canvas4");
          console.log("hi");
          this.drawLine(
            (this.$refs.table3.offsetWidth / this.topYearB) * this.currentYearB,
            "canvas3",
            90,0
          );
        }
      });
    },
    chooseAnswer(type) {
      if (type === "A") {
        if (this.slide === 1) {
          if (this.step === 0) {
            this.currentYear = this.currentYear - 10;
          } else if (this.step === 1) {
            this.slide = 2;
            // this.clearCanvas("canvas4");
            this.stepDirection++;
            // return
          } else if (this.step === 2) {
            this.currentYear--;
          } else if (this.step >= 3) {
            if (
              (this.currentYear > 0 && this.currentYear <= 1) ||
              (this.currentYear > 9 && this.currentYear <= 10) ||
              this.currentYear % 1 === 0.5 ||
              this.selected[this.selected.length - 1] != type
            ) {
              this.currentYear = this.currentYear - 0.5;
            } else if (this.currentYear === 0) {
              this.slide = 2;
              this.stepDirection++;
            } else {
              this.currentYear--;
            }
          }
        } else if (this.slide === 2) {
          if (this.stepDirection <= 1) {
            if (this.stepB === 1) {
              this.currentYearB = this.currentYearB - 5;
            } else if (this.stepB === 2) {
              this.currentYearB--;
            } else if (this.stepB >= 3) {
              if (
                (this.currentYearB > 0 && this.currentYearB <= 1) ||
                (this.currentYearB > 9 && this.currentYearB <= 10) ||
                this.currentYearB % 1 === 0.5 ||
                this.selected[this.selected.length - 1] != type
              ) {
                this.currentYearB = this.currentYearB - 0.5;
              } else if (this.currentYearB === 0) {
                return;
              } else {
                this.currentYearB--;
              }
            }
          } else {
            if (this.stepB === 0) {
              this.stepB++;
              return;
            } else {
              if (
                (this.currentYearB > 0 && this.currentYearB <= 1) ||
                (this.currentYearB > 9 && this.currentYearB <= 10) ||
                this.currentYearB % 1 === 0.5 ||
                this.selected[this.selected.length - 1] != type
              ) {
                this.currentYearB = this.currentYearB - 0.5;
              } else if (this.currentYearB === 0) {
                return;
              } else {
                this.currentYearB--;
              }
            }
          }
        }
      } else if (type === "B") {
        if (this.slide === 1) {
          if (this.step === 0) {
            return;
          } else if (this.step === 1) {
            this.currentYear = this.currentYear + 5;
          } else if (this.step === 2) {
            this.currentYear++;
          } else if (this.step >= 3) {
            if (
              (this.currentYear >= 0 && this.currentYear < 1) ||
              (this.currentYear >= 9 && this.currentYear < 10) ||
              this.currentYear % 1 === 0.5 ||
              this.selected[this.selected.length - 1] != type
            ) {
              this.currentYear = this.currentYear + 0.5;
            } else if (this.currentYear >= 10) {
              return;
            } else {
              this.currentYear++;
            }
          }
        } else if (this.slide === 2) {
          if (this.currentYearB >= 10) {
            this.slide = 1;
            this.stepB = 0;
            this.currentYear = this.currentYear + 0.5;
          } else {
            if (this.stepDirection <= 1) {
              if (this.stepB >= 3) {
                if (
                  (this.currentYearB >= 0 && this.currentYearB < 1) ||
                  (this.currentYearB >= 9 && this.currentYearB < 10) ||
                  this.currentYearB % 1 === 0.5 ||
                  this.selected[this.selected.length - 1] != type
                ) {
                  this.currentYearB = this.currentYearB + 0.5;
                } else {
                  this.currentYearB++;
                }
              } else {
                this.currentYearB++;
              }
            } else {
              if (
                (this.currentYearB >= 0 && this.currentYearB < 1) ||
                (this.currentYearB >= 9 && this.currentYearB < 10) ||
                this.currentYearB % 1 === 0.5 ||
                this.selected[this.selected.length - 1] != type
              ) {
                this.currentYearB = this.currentYearB + 0.5;
              } else {
                this.currentYearB++;
                console.log("here ...");
              }
            }
          }
        }
      } else {
        alert("A&B");
        return;
      }
      this.selected.push(type);
      this.step++;
      if (this.slide === 2) {
        this.stepB++;
      }
      this.clearCanvas("canvas1");
      this.clearCanvas("canvas3");

      if (this.currentYear > 0 && this.slide === 1) {
        this.$nextTick(() => {
          this.drawLine(
            (this.$refs.table1.offsetWidth / this.topYear) * this.currentYear,
            "canvas1",
            90,0
          );
        });
      }
      if (this.currentYearB > 0 && this.slide === 2) {
        this.$nextTick(() => {
          this.setCanvasWidth(this.$refs.table3.offsetWidth, "canvas3");
          this.clearCanvas("canvas3");
          this.drawLine(
            (this.$refs.table3.offsetWidth / this.topYearB) * this.currentYearB,
            "canvas3",
            90,0
          );
          this.setCanvasWidth(this.$refs.table4.offsetWidth, "canvas4");
          this.clearCanvas("canvas4");
          this.drawLine(
           this.$refs.table4.offsetWidth/2,
            "canvas4",
            10,0
          );
          this.drawLine(
           this.$refs.table4.offsetWidth/2,
            "canvas4",
            10,this.$refs.table4.offsetWidth/2
          );
        });
      }
    },

    drawLine(width, cvs, tpos, lpos) {
      //获取画板
      var canvas = document.getElementById(cvs);

      if (canvas == null) return false;
      //获取画笔
      var ctx = canvas.getContext("2d");
      //开始绘制新路径
      ctx.beginPath();
      //画线
      //横  （向右）
      drawArrowLine(cvs, 0, tpos, 0+lpos+5, 0, width+lpos-5, 0);
      //横  （向左）
      drawArrowLine(cvs, 0+lpos+5, 0, 5, 0, 0, 0);
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
    clearCanvas(cvs) {
      //获取画板
      var canvas = document.getElementById(cvs);
      if (canvas == null) return false;
      //清除画布内容
      canvas.height = canvas.height;
    },
    setCanvasWidth(width, cvs) {
      //获取画板
      var canvas = document.getElementById(cvs);
      if (canvas == null) return false;
      //清除画布内容
      canvas.width = width;
      canvas.height = canvas.height;
    }
  },
  mounted() {
    this.setCanvasWidth(this.$refs.table1.offsetWidth, "canvas1");
    this.clearCanvas("canvas1");
    this.drawLine(this.$refs.table1.offsetWidth, "canvas1", 90,0);
    this.setCanvasWidth(this.$refs.table2.offsetWidth, "canvas2");
    this.clearCanvas("canvas2");
    this.drawLine(this.$refs.table2.offsetWidth, "canvas2", 10,0);
  },
  computed: {
    allContent: function() {
      return function(year) {
        var arr = [];
        for (var i = 1; i <= 4 * year; i++) {
          arr.push(i);
        }
        return arr;
      };
    }
  }
};
</script>