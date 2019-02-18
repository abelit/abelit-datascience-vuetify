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
  </div>
</template>

<script>
export default {
  data: () => ({
    activeBtn: 1,
    showNav: true,
    picker: new Date().toISOString().substr(0, 10),
    picker2: new Date().toISOString().substr(0, 10),
    today: "2019-01-08",
    events: [
      {
        title: "Vacation",
        details: "Going to the beach!",
        date: "2018-12-30",
        open: false
      },
      {
        title: "Vacation",
        details: "Going to the beach!",
        date: "2018-12-31",
        open: false
      },
      {
        title: "Vacation",
        details: "Going to the beach!",
        date: "2019-01-01",
        open: false
      },
      {
        title: "Meeting",
        details: "Spending time on how we do not have enough time",
        date: "2019-01-07",
        open: false
      },
      {
        title: "30th Birthday",
        details: "Celebrate responsibly",
        date: "2019-01-03",
        open: false
      },
      {
        title: "New Year",
        details: "Eat chocolate until you pass out",
        date: "2019-01-01",
        open: false
      },
      {
        title: "Conference",
        details: "Mute myself the whole time and wonder why I am on this call",
        date: "2019-01-21",
        open: false
      },
      {
        title: "Hackathon",
        details: "Code like there is no tommorrow",
        date: "2019-02-01",
        open: false
      }
    ],
    labels: ["12am", "3am", "6am", "9am", "12pm", "3pm", "6pm", "9pm"],
    value: [200, 675, 410, 390, 310, 460, 250, 240],
    sheet: false,
    tiles: [
      { img: "keep.png", title: "Keep", url: "https://www.baidu.com" },
      { img: "inbox.png", title: "Inbox" },
      { img: "hangouts.png", title: "Hangouts" },
      { img: "messenger.png", title: "Messenger" },
      { img: "google.png", title: "Google+" }
    ]
  }),
  computed: {
    // convert the list of events into a map of lists keyed by date
    eventsMap() {
      const map = {};
      this.events.forEach(e => (map[e.date] = map[e.date] || []).push(e));
      return map;
    }
  },
  methods: {
    open(event) {
      alert(event.title);
    }
  }
};
</script>

<script>
export default {
  data: () => ({
    activeBtn: 1,
    showNav: true,
    picker: new Date().toISOString().substr(0, 10),
    picker2: new Date().toISOString().substr(0, 10),
    today: "2019-01-08",
    events: [
      {
        title: "Vacation",
        details: "Going to the beach!",
        date: "2018-12-30",
        open: false
      },
      {
        title: "Vacation",
        details: "Going to the beach!",
        date: "2018-12-31",
        open: false
      },
      {
        title: "Vacation",
        details: "Going to the beach!",
        date: "2019-01-01",
        open: false
      },
      {
        title: "Meeting",
        details: "Spending time on how we do not have enough time",
        date: "2019-01-07",
        open: false
      },
      {
        title: "30th Birthday",
        details: "Celebrate responsibly",
        date: "2019-01-03",
        open: false
      },
      {
        title: "New Year",
        details: "Eat chocolate until you pass out",
        date: "2019-01-01",
        open: false
      },
      {
        title: "Conference",
        details: "Mute myself the whole time and wonder why I am on this call",
        date: "2019-01-21",
        open: false
      },
      {
        title: "Hackathon",
        details: "Code like there is no tommorrow",
        date: "2019-02-01",
        open: false
      }
    ],
    labels: ["12am", "3am", "6am", "9am", "12pm", "3pm", "6pm", "9pm"],
    value: [200, 675, 410, 390, 310, 460, 250, 240],
    sheet: false,
    tiles: [
      { img: "keep.png", title: "Keep", url: "https://www.baidu.com" },
      { img: "inbox.png", title: "Inbox" },
      { img: "hangouts.png", title: "Hangouts" },
      { img: "messenger.png", title: "Messenger" },
      { img: "google.png", title: "Google+" }
    ]
  }),
  computed: {
    // convert the list of events into a map of lists keyed by date
    eventsMap() {
      const map = {};
      this.events.forEach(e => (map[e.date] = map[e.date] || []).push(e));
      return map;
    }
  },
  methods: {
    open(event) {
      alert(event.title);
    }
  }
};
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
