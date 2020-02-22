<template>
  <div class="text-center">
    <v-menu
      offset-y
      max-width="800"
      bottom
      allow-overflow
      :close-on-content-click="false"
    >
      <template v-slot:activator="{ on }">
        <v-row v-on="on">
          <v-col cols="12" sm="4">
            <v-text-field v-model="timeRangeText" label="Time range" prepend-icon="event" readonly></v-text-field>
          </v-col>
        </v-row>
      </template>
      <v-row justify="center">
        <v-col cols="12" sm="2" class="pt-8">
          <v-btn text block left @click="setTime(1)">最近15分钟</v-btn>
          <v-btn text block left @click="setTime(2)">最近30分钟</v-btn>
          <v-btn text block left @click="setTime(3)">最近1小时</v-btn>
          <v-btn text block left @click="setTime(4)">最近3小时</v-btn>
          <v-btn text block left @click="setTime(5)">最近6小时</v-btn>
          <v-btn text block left @click="setTime(6)">最近12小时</v-btn>
          <v-btn text block left @click="setTime(7)">最近24小时</v-btn>
        </v-col>
        <v-col cols="12" sm="5">
          <v-row justify="center">开始时间</v-row>
          <v-row justify="center" class="pt-2">
            <v-time-picker v-model="startPicker" :max="endPicker" format="24hr"></v-time-picker>
          </v-row>
        </v-col>
        <v-col cols="12" sm="5">
          <v-row justify="center">结束时间</v-row>
          <v-row justify="center" class="pt-2">
            <v-time-picker v-model="endPicker" :min="startPicker" format="24hr"></v-time-picker>
          </v-row>
        </v-col>
      </v-row>
      <!-- <v-row class="pr-7 pb-2">
        <v-spacer></v-spacer>
        <v-btn color="success" @click="$refs.menu.save(dates)">确定</v-btn>
        <v-btn color="success" @click="menu = false">取消</v-btn>
      </v-row> -->
    </v-menu>
  </div>
</template>


<script>
import { subDays } from "date-fns";
export default {
  data: () => ({
    dates: [],
    startPicker: null,
    endPicker: null,
  }),
  computed: {
    timeRangeText() {
      this.dates = [this.startPicker, this.endPicker];
      if (this.startPicker == null || !this.endPicker == null) {
        return "";
      }
      return this.dates.join(" ~ ");
    }
  },
  methods: {
    setTime(param) {
      switch (param) {
        case 1:
          this.startPicker = new Date(new Date().getTime() - 15*60*1000).toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          this.endPicker = new Date().toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          break;
        case 2:
          this.startPicker = new Date(new Date().getTime() - 30*60*1000).toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          this.endPicker = new Date().toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          break;
        case 3:
          this.startPicker = new Date(new Date().getTime() - 1*60*60*1000).toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          this.endPicker = new Date().toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          break;
        case 4:
          this.startPicker = new Date(new Date().getTime() - 3*60*60*1000).toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          this.endPicker = new Date().toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          break;
        case 5:
          this.startPicker = new Date(new Date().getTime() - 6*60*60*1000).toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          this.endPicker = new Date().toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          break;
         case 6:
          this.startPicker = new Date(new Date().getTime() - 12*60*60*1000).toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          this.endPicker = new Date().toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          break;
         case 7:
          this.startPicker = new Date(new Date().getTime() - 24*60*60*1000).toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          this.endPicker = new Date().toLocaleTimeString('chinese', { hour12: false }).substr(0,5)
          break;
        default:
          this.startPicker = null;
          this.endPicker = null;
      }
    },
    
  },
  mounted() {
    console.log(new Date());
  }
};
</script>