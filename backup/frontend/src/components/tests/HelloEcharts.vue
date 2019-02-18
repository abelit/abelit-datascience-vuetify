<template>
<div id="myChart" :style="{width: '800px', height: '400px'}"></div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloEcharts',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      goods: {}
    }
  },
  mounted () {
    this.drawLine()
  },
  created () {
    axios.get('./static/data/dat.json').then(res => {
      const data = res.data
      this.goods = data
      console.log(this.goods)
      console.log(Array.from(this.goods.xAxis.data))
    })
  },
  methods: {
    drawLine () {
      // 基于准备好的dom，初始化echarts实例
      let myChart = this.$echarts.init(document.getElementById('myChart'))
      // 绘制图表
      myChart.setOption({
        title: {},
        tooltip: {},
        xAxis: {
          data: []
        },
        yAxis: {},
        series: [{
          name: '销量',
          type: 'bar',
          data: []
        }]
      })
      myChart.showLoading()

      axios.get('./static/data/dat.json').then((res) => {
        setTimeout(() => {
          const data = res.data
          const list = data.series.map(good => {
            let list = good.data
            return [...list]
          })
          console.log(list)
          console.log(Array.from(...list))
          myChart.hideLoading()
          myChart.setOption({
            title: data.title,
            xAxis: [{
              data: data.xAxis.data
            }],
            series: [{
              name: '销量',
              type: 'bar',
              data: Array.from(...list)
            }]
          })
        }, 3000)
      })
    }
  }
}
</script>
