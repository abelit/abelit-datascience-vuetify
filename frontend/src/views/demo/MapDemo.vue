<template>
<div id="helloword">
  <h1>Test Vue ECharts Map</h1>
  <div style="z-index: 1000" id="map">
 
  </div>
 
  <div style="z-index: 2000" id="map1"></div>
</div>
</template>

<script>
import cst001 from '@/assets/map/cst001.json'
// import csta from '@/assets/map/csta.json'
export default {
  name: 'TestEchartsMap',
  data () {
    return {
      msg: [{
        name: 'A',
        value: 4822000
      },
      {
        name: 'B',
        value: 73144900
      },
      {
        name: 'C',
        value: 6553
      },
      {
        name: 'D',
        value: 29491310
      }
    ]
  }
  },
  watch: {},
  methods: {
    initEchart () {
      let option = {
        title: {
          text: 'Custom Map 001 Demo',
          subtext: 'Data from www.dataforum.org',
          sublink: 'http://www.census.gov/popest/data/datasets.html',
          left: 'center'
        },
        tooltip: {
          trigger: 'item',
          showDelay: 0,
          transitionDuration: 0.2,
          formatter: function( params ) {
            var value = (params.value + '').split('.')
            value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,')
            return params.seriesName + '<br/>' + params.name + ': ' + value
          }
        },
        visualMap: {
          left: 'right',
          min: 500000,
          max: 38000000,
          inRange: {
            color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
          },
          text: ['High', 'Low'], // 文本，默认为数值文本
          calculable: true
        },
        toolbox: {
          show: true,
          left: 'left',
          top: 'top',
          feature: {
            dataView: {
              readOnly: false
            },
            restore: {},
            saveAsImage: {}
          }
        },
        series: [{
          name: 'Custom Map 001 PopEstimates',
          type: 'map',
          roam: true,
          map: 'cstmap',
          itemStyle: {
            emphasis: {
              label: {
                show: true
              }
            }
          },
          // 文本位置修正
          textFixed: {
            A: [20, -20]
          },
          data: this.$data.msg
        }]
      }
      let myChartMap = this.$echarts.init(document.getElementById('map'))
      this.$echarts.registerMap('cstmap', cst001)
      // myChartMap.showLoading()
      myChartMap.setOption(option)
      // myChartMap.hideLoading()
    },
    initEchartNew () {
      let option = {
        title: {
          text: 'Custom Map 002 Demo',
          subtext: 'Data from www.dataforum.org',
          sublink: 'http://www.census.gov/popest/data/datasets.html',
          left: 'center'
        },
        tooltip: {
          trigger: 'item',
          showDelay: 0,
          transitionDuration: 0.2,
          formatter: function( params ) {
            var value = (params.value + '').split('.')
            value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,')
            return params.seriesName + '<br/>' + params.name + ': ' + value
          }
        },
        visualMap: {
          left: 'right',
          min: 500000,
          max: 38000000,
          inRange: {
            color: ['#334495', '#56w5b4', '#25g764', '#abd9e9', '#ffrtg3', '#drtt46', '#fee090', '#234gdg', '#ffgd4t', '#ertnh5', '#a55nhy']
          },
          text: ['High', 'Low'], // 文本，默认为数值文本
          calculable: true
        },
        toolbox: {
          show: true,
          left: 'left',
          top: 'top',
          feature: {
            dataView: {
              readOnly: false
            },
            restore: {},
            saveAsImage: {}
          }
        },
        series: [{
          name: 'Custom Map 001 PopEstimates',
          type: 'map',
          roam: true,
          map: 'cstmap',
          itemStyle: {
            emphasis: {
              label: {
                show: true
              }
            }
          },
          // 文本位置修正
          textFixed: {
            A: [20, -20]
          },
          data: this.$data.msg
        }]
      }
      let myChartMap = this.$echarts.init(document.getElementById('map1'))
      this.$echarts.registerMap('cstmap', cst001)
      // myChartMap.showLoading()
      myChartMap.setOption(option)
      // myChartMap.hideLoading()
    }
 
  },
  filters: {
  },
  computed: {
  },
  created () {
  },
  mounted () {
      this.initEchart()
            this.initEchartNew()

  }
}
</script>

<style scoped>
#map1{
    position: absolute;
  width: 600px;
  height: 600px;
  float: left;
}
#map{
     position: absolute;
  width: 600px;
  height: 600px;
  margin-top: 20px;
  float: left;
}
</style>
