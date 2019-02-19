<template>
  <div class>
    <div>
      <h1 class="abelit">Hi Abelit! Welcome to Vue and Vuetify!</h1>
    </div>
    <div class="text-xs-left m1">
      <v-btn color="success">Success</v-btn>
      <v-btn color="error">Error</v-btn>
      <v-btn color="warning">Warning</v-btn>
      <v-btn color="info">Info</v-btn>
    </div>
    <div class="text-xs-left">
      <v-btn fab dark small color="primary">
        <v-icon dark>remove</v-icon>
      </v-btn>

      <v-btn fab dark small color="pink">
        <v-icon dark>favorite</v-icon>
      </v-btn>

      <v-btn fab dark color="indigo">
        <v-icon dark>add</v-icon>
      </v-btn>

      <v-btn fab dark color="teal">
        <v-icon dark>list</v-icon>
      </v-btn>

      <v-btn fab dark large color="cyan">
        <v-icon dark>edit</v-icon>
      </v-btn>

      <v-btn fab dark large color="purple">
        <v-icon dark>android</v-icon>
      </v-btn>
    </div>

    <div class="text-xs-center">
      <v-btn
        :loading="loading"
        :disabled="loading"
        color="secondary"
        @click="loader = 'loading'"
      >Accept Terms</v-btn>

      <v-btn
        :loading="loading3"
        :disabled="loading3"
        color="blue-grey"
        class="white--text"
        @click="loader = 'loading3'"
      >Upload
        <v-icon right dark>cloud_upload</v-icon>
      </v-btn>

      <v-btn :loading="loading2" :disabled="loading2" color="success" @click="loader = 'loading2'">
        Custom Loader
        <span slot="loader">Loading...</span>
      </v-btn>

      <v-btn :loading="loading4" :disabled="loading4" color="info" @click="loader = 'loading4'">
        Icon Loader
        <span slot="loader" class="custom-loader">
          <v-icon light>cached</v-icon>
        </span>
      </v-btn>
    </div>
    <div class="text-xs-left">
      <v-layout>
        <v-flex xs12 sm6 offset-sm3>
          <v-card>
            <v-img src="https://cdn.vuetifyjs.com/images/cards/desert.jpg" aspect-ratio="2.75"></v-img>

            <v-card-title primary-title>
              <div>
                <h3 class="headline mb-0">Kangaroo Valley Safari</h3>
                <div>Located two hours south of Sydney in the
                  <br>Southern Highlands of New South Wales, ...
                </div>
              </div>
            </v-card-title>

            <v-card-actions>
              <v-btn flat color="orange">Share</v-btn>
              <v-btn flat color="orange">Explore</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </div>
    
    

    <div class>
      <v-card class="hide-overflow" height="200px">
        <v-card-text class="text-xs-center">
          <v-btn flat color="primary" @click="showNav = !showNav">Toggle Nav</v-btn>
        </v-card-text>

        <v-bottom-nav
          :active.sync="activeBtn"
          :value="showNav"
          absolute
          color="transparent"
          locale="zh-cn"
        >
          <v-btn flat color="teal">
            <span>Recents</span>
            <v-icon>history</v-icon>
          </v-btn>

          <v-btn flat color="teal">
            <span>Favorites</span>
            <v-icon>favorite</v-icon>
          </v-btn>

          <v-btn flat color="teal">
            <span>Nearby</span>
            <v-icon>place</v-icon>
          </v-btn>
        </v-bottom-nav>
      </v-card>
    </div>



    <div>
      <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Books</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Book</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <button type="button" class="btn btn-warning btn-sm">Update</button>
                <button type="button" class="btn btn-danger btn-sm">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
    </div>

  <div>
    <v-footer
    dark
    height="auto"
  >
    <v-card
      class="flex"
      flat
      tile
    >
      <v-card-title class="teal">
        <strong class="subheading">Get connected with us on social networks!</strong>

        <v-spacer></v-spacer>

        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-3"
          dark
          icon
        >
          <v-icon size="24px">{{ icon }}</v-icon>
        </v-btn>
      </v-card-title>

      <v-card-actions class="grey darken-3 justify-center">
        &copy;2018 — <strong>Vuetify</strong>
      </v-card-actions>
    </v-card>
  </v-footer>
  </div>


  <div>
    <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-card
      dark
      flat
    >
      <v-btn
        absolute
        bottom
        color="pink"
        right
        fab
      >
        <v-icon>mdi-plus</v-icon>
      </v-btn>
      <v-card-title class="pa-2 purple lighten-3">
        <v-btn icon>
          <v-icon>mdi-menu</v-icon>
        </v-btn>
        <h3 class="title font-weight-light text-xs-center grow">Timeline</h3>
        <v-avatar>
          <v-img src="https://avataaars.io/?avatarStyle=Circle&topType=LongHairStraight&accessoriesType=Blank&hairColor=BrownDark&facialHairType=Blank&clotheType=BlazerShirt&eyeType=Default&eyebrowType=Default&mouthType=Default&skinColor=Light"></v-img>
        </v-avatar>
      </v-card-title>
      <v-img
        src="https://cdn.vuetifyjs.com/images/cards/forest.jpg"
        gradient="to top, rgba(0,0,0,.44), rgba(0,0,0,.44)"
      >
        <v-container fill-height>
          <v-layout align-center>
            <strong class="display-4 font-weight-regular mr-4">8</strong>
            <v-layout column justify-end>
              <div class="headline font-weight-light">Monday</div>
              <div class="text-uppercase font-weight-light">February 2015</div>
            </v-layout>
          </v-layout>
        </v-container>
      </v-img>
    </v-card>
    <v-card-text class="py-0">
      <v-timeline
        align-top
        dense
      >
        <v-timeline-item
          color="pink"
          small
        >
          <v-layout pt-3>
            <v-flex xs3>
              <strong>5pm</strong>
            </v-flex>
            <v-flex>
              <strong>New Icon</strong>
              <div class="caption">Mobile App</div>
            </v-flex>
          </v-layout>
        </v-timeline-item>

        <v-timeline-item
          color="teal lighten-3"
          small
        >
          <v-layout wrap pt-3>
            <v-flex xs3>
              <strong>3-4pm</strong>
            </v-flex>
            <v-flex>
              <strong>Design Stand Up</strong>
              <div class="caption mb-2">Hangouts</div>
              <v-avatar>
                <v-img
                  src="https://avataaars.io/?avatarStyle=Circle&topType=LongHairFrida&accessoriesType=Kurt&hairColor=Red&facialHairType=BeardLight&facialHairColor=BrownDark&clotheType=GraphicShirt&clotheColor=Gray01&graphicType=Skull&eyeType=Wink&eyebrowType=RaisedExcitedNatural&mouthType=Disbelief&skinColor=Brown"
                ></v-img>
              </v-avatar>
              <v-avatar>

                <v-img
                  src="https://avataaars.io/?avatarStyle=Circle&topType=ShortHairFrizzle&accessoriesType=Prescription02&hairColor=Black&facialHairType=MoustacheMagnum&facialHairColor=BrownDark&clotheType=BlazerSweater&clotheColor=Black&eyeType=Default&eyebrowType=FlatNatural&mouthType=Default&skinColor=Tanned"
                ></v-img>
              </v-avatar>
              <v-avatar>
                <v-img
                  src="https://avataaars.io/?avatarStyle=Circle&topType=LongHairMiaWallace&accessoriesType=Sunglasses&hairColor=BlondeGolden&facialHairType=Blank&clotheType=BlazerSweater&eyeType=Surprised&eyebrowType=RaisedExcited&mouthType=Smile&skinColor=Pale"
                ></v-img>
              </v-avatar>
            </v-flex>
          </v-layout>
        </v-timeline-item>

        <v-timeline-item
          color="pink"
          small
        >
          <v-layout pt-3>
            <v-flex xs3>
              <strong>12pm</strong>
            </v-flex>
            <v-flex>
              <strong>Lunch break</strong>
            </v-flex>
          </v-layout>
        </v-timeline-item>

        <v-timeline-item
          color="teal lighten-3"
          small
        >
          <v-layout pt-3>
            <v-flex xs3>
              <strong>9-11am</strong>
            </v-flex>
            <v-flex>
              <strong>Finish Home Screen</strong>
              <div class="caption">Web App</div>
            </v-flex>
          </v-layout>
        </v-timeline-item>
      </v-timeline>
    </v-card-text>
  </v-card>
  </div>


  <div>
    <v-layout row wrap>
    <v-flex xs12 sm6>
      <v-date-picker v-model="picker" color="green lighten-1"></v-date-picker>
    </v-flex>
    <v-flex xs12 sm6 class="hidden-xs-only">
      <v-date-picker v-model="picker2" color="green lighten-1" header-color="primary" locale='zh-cn'></v-date-picker>
    </v-flex>
  </v-layout>
  </div>

  <div>
    <div class="text-xs-center">
    <v-pagination
      v-model="page"
      :length="6"
    ></v-pagination>
  </div>
  </div>


  <div>
    <div id="helloword">
  <h1>Test Vue ECharts Map</h1>
  <div id="map"></div>
</div>
  </div>

 <div id="countapp">
  <p>{{ count }}</p>
    <button @click="increment" type="button" class="btn btn-primary">+</button>
    <button @click="decrement" type="button" class="btn btn-primary">-</button>
</div>



  </div>
</template>


<script>
import axios from 'axios'
// 导入自定义地图数据
import cst001 from '../../static/map/cst001.json'
// 导入Vuex中sore状态信息
import store from '../store.js'

export default {
  data () {
    return {
      activeBtn: 1,
      showNav: true,
      icons: [
        'fab fa-facebook',
        'fab fa-twitter',
        'fab fa-google-plus',
        'fab fa-linkedin',
        'fab fa-instagram'
      ],
      picker: new Date().toISOString().substr(0, 10),
      picker2: new Date().toISOString().substr(0, 10),
      page: 1,
      books: [],
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
  methods: {
    getBooks () {
      const path = 'http://localhost:5000/books'
      axios.get(path)
        .then((res) => {
          this.books = res.data.books
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    },
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
    increment () {
      store.commit('increment')
    },
    decrement () {
    	store.commit('decrement')
    }
  },
  computed: {
    count () {
	    return store.state.count
    }
  },
  created () {
    this.getBooks()
  },
  mounted() {
    this.initEchart()
  },
}
</script>

<style lang="stylus" scoped>
mpdwidth = 100px;
lwidth = 50px;

div {
  h1 {
    padding-top: mpdwidth;
    padding-left: lwidth;
  }
}

.m1 {
  padding: mpdwidth;
}

.my-event {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  border-radius: 2px;
  background-color: #1867c0;
  color: #ffffff;
  border: 1px solid #1867c0;
  width: 100%;
  font-size: 12px;
  padding: 3px;
  cursor: pointer;
  margin-bottom: 1px;
}

.v-sheet--offset {
  top: -24px;
  position: relative;
}
</style>

<style lang="scss">
$mpdwidth: 80px;
$ldwidth: 50px;
div {
  h1 {
    padding-top: $mpdwidth;
    padding-left: $ldwidth;
  }
}
.haha {
  width: 6 * $ldwidth;
}
</style>

<style lang="less" scoped>
@fsize: 42px;
.haha1 {
  font-size: @fsize;
}
</style>


<style scoped>
/* This is for documentation purposes and will not be needed in your application */
#create .v-speed-dial {
  position: absolute;
}

#create .v-btn--floating {
  position: relative;
}
</style>


<style scoped>
#map {
  width: 100%;
  height: 600px;
  margin-top: 10px;
  float: left;
}
</style>

<style lang="css" scoped>
#countapp {
  color: #dddddd;
}
#countapp p {
  font-size: 48px;
}
#countapp button {
  color: #fdcabd;
}
</style>