<template>
<div id="helloword" class="container">
  <h1>Test Vue ECharts Map</h1>
  <div class="btn-group" data-toggle="buttons">
  	<label class="btn btn-primary">
  		<input type="radio" name="options" id="option1"> 选项 1
  	</label>
  	<label class="btn btn-primary">
  		<input type="radio" name="options" id="option2"> 选项 2
  	</label>
  	<label class="btn btn-primary">
  		<input type="radio" name="options" id="option3"> 选项 3
  	</label>
    <label class="btn btn-primary">
  		<input type="radio" name="options" id="option3"> {{ now() }}
  	</label>
  </div>
  <div class="btn-group" role="group" aria-label="Basic example">
  <button type="button" class="btn btn-secondary">Left</button>
  <button type="button" class="btn btn-secondary">Middle</button>
  <button type="button" class="btn btn-secondary">Right</button>
</div>
<div class="card" style="width: 18rem;">
  <img class="card-img-top" src="#" alt="Card image cap">
  <div class="card-body">
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
  </div>
</div>
<div class="progress">
 <div class="progress-bar w-75" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item">
      <a class="page-link" href="#" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
        <span class="sr-only">Previous</span>
      </a>
    </li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
        <span class="sr-only">Next</span>
      </a>
    </li>
  </ul>
</nav>
  <div id="map"></div>
</div>
</template>

<script>
import cst001 from '../../../static/map/cst001.json'
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
    now: function () {
      var d = new Date()
      return d.toUTCString()
    }
  },
  filters: {
  },
  computed: {
    initEchart: function() {
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
    }
    // now: function () {
    //   return Date.now()
    // }
  },
  created () {
    console.log('created ...............')
  },
  mounted () {
    // this.initEchart()
    this.initEchart
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
