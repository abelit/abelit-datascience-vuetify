<template>
<div class="">
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
    <v-btn :loading="loading" :disabled="loading" color="secondary" @click="loader = 'loading'">
      Accept Terms
    </v-btn>

    <v-btn :loading="loading3" :disabled="loading3" color="blue-grey" class="white--text" @click="loader = 'loading3'">
      Upload
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
              <div>Located two hours south of Sydney in the <br>Southern Highlands of New South Wales, ...</div>
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
  <div class="">
    <v-card class="hide-overflow" height="200px">
      <v-card-text class="text-xs-center">
        <v-btn flat color="primary" @click="showNav = !showNav">
          Toggle Nav
        </v-btn>
      </v-card-text>

      <v-bottom-nav :active.sync="activeBtn" :value="showNav" absolute color="transparent" locale='zh-cn'>
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
  <div class="">
    <v-layout>
      <v-flex>
        <v-sheet height="500">
          <v-calendar :now="today" :value="today" color="primary" locale='zh-cn'>
            <template slot="day" slot-scope="{ date }">
              <template v-for="event in eventsMap[date]">
                <v-menu :key="event.title" v-model="event.open" full-width offset-x>
                  <div v-if="!event.time" slot="activator" v-ripple class="my-event" v-html="event.title"></div>
                  <v-card color="grey lighten-4" min-width="350px" flat>
                    <v-toolbar color="primary" dark>
                      <v-btn icon>
                        <v-icon>edit</v-icon>
                      </v-btn>
                      <v-toolbar-title v-html="event.title"></v-toolbar-title>
                      <v-spacer></v-spacer>
                      <v-btn icon>
                        <v-icon>favorite</v-icon>
                      </v-btn>
                      <v-btn icon>
                        <v-icon>more_vert</v-icon>
                      </v-btn>
                    </v-toolbar>
                    <v-card-title primary-title>
                      <span v-html="event.details"></span>
                    </v-card-title>
                    <v-card-actions>
                      <v-btn flat color="secondary">
                        Cancel
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-menu>
              </template>
            </template>
          </v-calendar>
        </v-sheet>
      </v-flex>
    </v-layout>
  </div>
  <div class="">
    <v-layout row wrap>
      <v-flex xs12 sm6>
        <v-date-picker v-model="picker" color="green lighten-1" locale='zh-cn'></v-date-picker>
      </v-flex>
      <v-flex xs12 sm6 class="hidden-xs-only">
        <v-date-picker v-model="picker2" color="green lighten-1" header-color="primary"></v-date-picker>
      </v-flex>
    </v-layout>
  </div>
  <div class="">
    <template>
      <v-progress-linear :indeterminate="true"></v-progress-linear>
</template>
  </div>
  <div class="">
    <template>
  <div class="text-xs-center">
    <v-rating v-model="rating"></v-rating>
  </div>
</template>
  </div>
  <div class="">
    <template>
  <v-card
    class="mt-3 mx-auto"
    max-width="400"
  >
    <v-sheet
      class="v-sheet--offset mx-auto"
      color="cyan"
      elevation="12"
      max-width="calc(100% - 32px)"
    >
      <v-sparkline
        :labels="labels"
        :value="value"
        color="white"
        line-width="2"
        padding="16"
      ></v-sparkline>
    </v-sheet>

    <v-card-text class="pt-0">
      <div class="title font-weight-light mb-2">User Registrations</div>
      <div class="subheading font-weight-light grey--text">Last Campaign Performance</div>
      <v-divider class="my-2"></v-divider>
      <v-icon
        class="mr-2"
        small
      >
        mdi-clock
      </v-icon>
      <span class="caption grey--text font-weight-light">last registration 26 minutes ago</span>
    </v-card-text>
  </v-card>
</template>
  </div>
  <div class="">
    <template>
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
</template>
  </div>

  <div class="haha">
    <template>
  <div>
    <v-alert
      :value="true"
      color="success"
      icon="check_circle"
      outline
      class="haha1"
    >
      This is a success alert.
    </v-alert>

    <v-alert
      :value="true"
      color="info"
      icon="info"
      outline
    >
      This is an info alert.
    </v-alert>

    <v-alert
      :value="true"
      color="warning"
      icon="priority_high"
      outline
    >
      This is a warning alert.
    </v-alert>

    <v-alert
      :value="true"
      color="error"
      icon="warning"
      outline
    >
      This is a error alert.
    </v-alert>
  </div>
</template>
  </div>
  <div class="">
    <template>
  <div class="text-xs-center">
    <v-bottom-sheet v-model="sheet">
      <v-btn
        slot="activator"
        color="purple"
        dark
      >
        Click me
      </v-btn>

      <v-list>
        <v-subheader>Open in</v-subheader>
        <v-list-tile
          v-for="tile in tiles"
          :key="tile.title"
          @click="sheet = false"
        >
          <v-list-tile-avatar>
            <v-avatar size="32px" tile>
              <img
                :src="`https://cdn.vuetifyjs.com/images/bottom-sheets/${tile.img}`"
                :alt="tile.title"
              >
            </v-avatar>
          </v-list-tile-avatar>
          <v-list-tile-title>{{ tile.title }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-bottom-sheet>
  </div>
</template>

<div class="">
  <template>
  <v-card id="create">
    <v-container fluid grid-list-md>
      <v-layout child-flex wrap>
        <v-flex xs12 sm6 md4>
          <v-subheader>Options</v-subheader>
          <v-checkbox v-model="hover" label="Open on hover" hide-details></v-checkbox>
        </v-flex>
        <v-flex xs12 sm6 md4>
          <v-subheader>FAB location</v-subheader>
          <v-checkbox v-model="top" label="Top" hide-details></v-checkbox>
          <v-checkbox v-model="right" label="Right" hide-details></v-checkbox>
          <v-checkbox v-model="bottom" label="Bottom" hide-details></v-checkbox>
          <v-checkbox v-model="left" label="Left" hide-details></v-checkbox>
        </v-flex>
        <v-flex xs12 sm6 md4>
          <v-subheader>Speed dial direction</v-subheader>
          <v-radio-group v-model="direction" hide-details>
            <v-radio value="top" label="Top"></v-radio>
            <v-radio value="right" label="Right"></v-radio>
            <v-radio value="bottom" label="Bottom"></v-radio>
            <v-radio value="left" label="Left"></v-radio>
          </v-radio-group>
        </v-flex>
        <v-flex xs12 sm6 md4>
          <v-subheader>Transition</v-subheader>
          <v-radio-group v-model="transition" hide-details>
            <v-radio value="slide-y-transition" label="Slide y"></v-radio>
            <v-radio value="slide-y-reverse-transition" label="Slide y reverse"></v-radio>
            <v-radio value="slide-x-transition" label="Slide x"></v-radio>
            <v-radio value="slide-x-reverse-transition" label="Slide x reverse"></v-radio>
            <v-radio value="scale-transition" label="Scale"></v-radio>
          </v-radio-group>
        </v-flex>
      </v-layout>
    </v-container>
    <v-speed-dial
      v-model="fab"
      :top="top"
      :bottom="bottom"
      :right="right"
      :left="left"
      :direction="direction"
      :open-on-hover="hover"
      :transition="transition"
    >
      <v-btn
        slot="activator"
        v-model="fab"
        color="blue darken-2"
        dark
        fab
      >
        <v-icon>account_circle</v-icon>
        <v-icon>close</v-icon>
      </v-btn>
      <v-btn
        fab
        dark
        small
        color="green"
      >
        <v-icon>edit</v-icon>
      </v-btn>
      <v-btn
        fab
        dark
        small
        color="indigo"
      >
        <v-icon>add</v-icon>
      </v-btn>
      <v-btn
        fab
        dark
        small
        color="red"
      >
        <v-icon>delete</v-icon>
      </v-btn>
    </v-speed-dial>
  </v-card>
</template>
</div>
  </div>
</div>

</template>

<script>
export default {
  data: () => ({
    activeBtn: 1,
    showNav: true,
    picker: new Date().toISOString().substr(0, 10),
    picker2: new Date().toISOString().substr(0, 10),
    today: '2019-01-08',
    events: [{
        title: 'Vacation',
        details: 'Going to the beach!',
        date: '2018-12-30',
        open: false
      },
      {
        title: 'Vacation',
        details: 'Going to the beach!',
        date: '2018-12-31',
        open: false
      },
      {
        title: 'Vacation',
        details: 'Going to the beach!',
        date: '2019-01-01',
        open: false
      },
      {
        title: 'Meeting',
        details: 'Spending time on how we do not have enough time',
        date: '2019-01-07',
        open: false
      },
      {
        title: '30th Birthday',
        details: 'Celebrate responsibly',
        date: '2019-01-03',
        open: false
      },
      {
        title: 'New Year',
        details: 'Eat chocolate until you pass out',
        date: '2019-01-01',
        open: false
      },
      {
        title: 'Conference',
        details: 'Mute myself the whole time and wonder why I am on this call',
        date: '2019-01-21',
        open: false
      },
      {
        title: 'Hackathon',
        details: 'Code like there is no tommorrow',
        date: '2019-02-01',
        open: false
      }
    ],
    labels: [
      '12am',
      '3am',
      '6am',
      '9am',
      '12pm',
      '3pm',
      '6pm',
      '9pm'
    ],
    value: [
      200,
      675,
      410,
      390,
      310,
      460,
      250,
      240
    ],
    sheet: false,
      tiles: [
        { img: 'keep.png', title: 'Keep',url: 'https://www.baidu.com' },
        { img: 'inbox.png', title: 'Inbox' },
        { img: 'hangouts.png', title: 'Hangouts' },
        { img: 'messenger.png', title: 'Messenger' },
        { img: 'google.png', title: 'Google+' }
      ]
  }),
  computed: {
    // convert the list of events into a map of lists keyed by date
    eventsMap() {
      const map = {}
      this.events.forEach(e => (map[e.date] = map[e.date] || []).push(e))
      return map
    }
  },
  methods: {
    open(event) {
      alert(event.title)
    }
  }
}
</script>

<script>
  export default {
    data: () => ({
      direction: 'top',
      fab: false,
      fling: false,
      hover: false,
      tabs: null,
      top: false,
      right: true,
      bottom: true,
      left: false,
      transition: 'slide-y-reverse-transition'
    }),

    computed: {
      activeFab () {
        switch (this.tabs) {
          case 'one': return { 'class': 'purple', icon: 'account_circle' }
          case 'two': return { 'class': 'red', icon: 'edit' }
          case 'three': return { 'class': 'green', icon: 'keyboard_arrow_up' }
          default: return {}
        }
      }
    },

    watch: {
      top (val) {
        this.bottom = !val
      },
      right (val) {
        this.left = !val
      },
      bottom (val) {
        this.top = !val
      },
      left (val) {
        this.right = !val
      }
    }
  }
</script>

<style lang="stylus" scoped>
  mpdwidth = 100px
  lwidth = 50px;
  div {
    h1 {
      padding-top: mpdwidth;
      padding-left:lwidth;
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
  width: 6*$ldwidth;
}
</style>

<style lang="less">
  @fsize: 42px;
  .haha1 {
    font-size: @fsize;
  }
</style>


<style>
  /* This is for documentation purposes and will not be needed in your application */
  #create .v-speed-dial {
    position: absolute;
  }

  #create .v-btn--floating {
    position: relative;
  }
</style>
