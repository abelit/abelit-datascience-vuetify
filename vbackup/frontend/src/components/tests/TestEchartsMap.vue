<template>
<div id="helloword">
  <h1>Test Vue ECharts Map</h1>
  <div id="map"></div>
</div>
</template>

<script>
import cst001 from '../../../static/map/cst001.json'
import csta from '../../../static/map/csta.json'
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
    getDownMap(){
    	let that = this;
    	let chart = that.$echarts.init(document.getElementById("map"));
    	let name = "A";
          let option = {
            geo: {
              map: mapa,
              label: {
                normal: {
                    show: true,
                    textStyle: {
                        color: '#fff',
                        fontSize: 20
                    }
                },
                emphasis: {
                    textStyle: {
                        color: '#fff'
                    }
                }
              },
              itemStyle: {
                normal: {
                  borderColor: 'rgba(147, 235, 248, 1)',
                  borderWidth: 1,
                  areaColor: {//背景色
                    type: 'radial',
                    x: 0.5,
                    y: 0.5,
                    r: 0.8,
                    colorStops: [{
                        offset: 0,
                        color: 'rgba(4, 129, 181, 0.2)' // 0% 处的颜色
                    }, {
                        offset: 1,
                        color: 'rgba(4, 129, 181, 0.4)' // 100% 处的颜色
                    }],
                    globalCoord: false // 缺省为 false
                  },
                  shadowColor: 'rgba(128, 217, 248, 1)',
                  shadowOffsetX: -2,
                  shadowOffsetY: 2,
                  shadowBlur: 10
                },
                emphasis: {
                  areaColor: '#389BB7',
                  borderWidth: 0
                }
              },
            },
            series: [
              {
                type: 'effectScatter',
                coordinateSystem: 'geo',
              }
            ]
          }
          that.$echarts.registerMap('mapa',csta);//这句是由于返回的时候点击某个按钮，又执行了这个方法，但是地图不能加载，所以我注册了一下，用的json 数据，可写可不写
          chart.setOption(option);//注意这句要放在registerMap后面，要不然地图就变成了双击才能下钻！！！！md，找了好久原因
    }
  },
  filters: {
  },
  computed: {
  },
  created () {
    console.log('created ...............')
  },
  mounted () {
    this.initEchart()
    console.log('mounted ..............')
  },
  destroyed () {
    console.log('destroyed ...............')
  },
  beforeCreate () {
    console.log('beforeCreate ......')
  },
  beforeDestroy () {
    console.log('beforeDestroy ........')
  },
  beforeMount () {
    console.log('beforeMount ..........')
  },
  updated () {
    console.log('updated ......')
  },
  beforeUpdate () {
    console.log('beforeUpdate .......')
  }
}
</script>

<style scoped>
#map {
  width: 100%;
  height: 600px;
  margin-top: 10px;
  float: left;
}
</style>
