<template>
  <div id="helloword">
    <h1>Test Vue ECharts Map</h1>
    <div id="map2"></div>

  </div>
</template>

<script>
import cstmap from '../../../static/map/cst001.js'
// export default {
//   components: {
//
//         },
//         data () {
//             return {
//                 font: '24'
//             }
//         },
//         props: {
//             width: {
//                 type: String,
//                 default: '200px'
//             },
//             height: {
//                 type: String,
//                 default: '400px'
//             }
//         },
//         watch: {},
//         methods: {
//             drawmap() {
//               let chartMap = document.getElementById('chartMap');
//                 let smap = document.getElementById('s-map');　　　　　　　　　 // 动态修改图表的宽高，达到自适应的效果　
//                 var resizeWorldMapContainer = function () {
//                     chartMap.style.width  = smap.clientWidth +'px';
//                     chartMap.style.height = smap.clientHeight + 'px';
//                 };
//                 resizeWorldMapContainer();
//                 // 注册可用的地图
//                 echarts.registerMap('cst001', cst001);
//                 let myChart = echarts.init(chartMap);
//                 myChart.showLoading();
//                 myChart.setOption({
//                   title: {
//             text: 'Custom Map 001 Demo',
//             subtext: 'Data from www.dataforum.org',
//             sublink: 'http://www.census.gov/popest/data/datasets.html',
//             left: 'center'
//         },
//         visualMap: {
//             left: 'right',
//             min: 500000,
//             max: 38000000,
//             inRange: {
//                 color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
//             },
//             text:['High','Low'],           // 文本，默认为数值文本
//             calculable: true
//         },
//         toolbox: {
//             show: true,
//             //orient: 'vertical',
//             left: 'left',
//             top: 'top',
//             feature: {
//                 dataView: {readOnly: false},
//                 restore: {},
//                 saveAsImage: {}
//             }
//         },
//         series: [
//             {
//                 name: 'Custom Map 001 PopEstimates',
//                 type: 'map',
//                 roam: true,
//                 map: 'cst001',
//                 itemStyle:{
//                     emphasis:{label:{show:true}}
//                 },
//                 // 文本位置修正
//                 textFixed: {
//                     A: [20, -20]
//                 },
//                 data:[
//                     {name: 'A', value: 48220},
//                     {name: 'B', value: 731449},
//                     {name: 'C', value: 6553255},
//                     {name: 'D', value: 2949131}
//                 ]
//             }
//         ]
//                 });
//                 window.addEventListener("resize", function(){
//                    resizeWorldMapContainer();
//                    myChart.resize();
//                })
//             }
//         },
//         filters: {},
//         computed: {},
//         created () {
//
//         },
//         mounted () {
//             this.drawmap()
//         },
//         destroyed () {}
// }
export default {
  name: 'TestEchartsMap',
  data() {
  },
  methods:{
    initEchart(){
      var myChartMap2 = this.$echarts.init(document.getElementById('map2'));
      // 地图上数据
      var myData = [
        {name: '分店1', value: [121.15, 31.89, 90]},
        {name: '分店2', value: [109.781327, 39.608266, 120]},
        {name: '分店3', value: [120.38, 37.35, 142]},
        {name: '分店4', value: [122.207216, 29.985295, 123]},
        {name:'分店5',value:[110.245672,30.7787677,566]}
      ]
      myChartMap2.setOption({
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
              formatter: function (params) {
                  var value = (params.value + '').split('.');
                  value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,');
                  return params.seriesName + '<br/>' + params.name + ': ' + value;
              }
          },
          visualMap: {
              left: 'right',
              min: 500000,
              max: 38000000,
              inRange: {
                  color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
              },
              text:['High','Low'],           // 文本，默认为数值文本
              calculable: true
          },
          toolbox: {
              show: true,
              //orient: 'vertical',
              left: 'left',
              top: 'top',
              feature: {
                  dataView: {readOnly: false},
                  restore: {},
                  saveAsImage: {}
              }
          },
          series: [
              {
                  name: 'Custom Map 001 PopEstimates',
                  type: 'map',
                  roam: true,
                  map: 'cstmap',
                  itemStyle:{
                      emphasis:{label:{show:true}}
                  },
                  // 文本位置修正
                  textFixed: {
                      A: [20, -20]
                  },
                  data:[
                      {name: 'A', value: 4822000},
                      {name: 'B', value: 73144900},
                      {name: 'C', value: 6553},
                      {name: 'D', value: 29491310}
                  ]
              }
          ]
      })
    },
  },
  mounted(){
    this.initEchart()
  },
}
</script>

<style scoped>
  #map2{
    width: 100%;
    height:600px;
    margin-top:10px;
    float: left;
  }
</style>
