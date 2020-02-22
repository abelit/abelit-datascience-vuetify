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
            <v-text-field v-model="dateRangeText" label="Date range" prepend-icon="event" readonly></v-text-field>
          </v-col>
        </v-row>
      </template>
      <v-row justify="center">
        <v-col cols="12" sm="2">
          <v-btn text block left @click="setDate(1)">今日</v-btn>
          <v-btn text block left @click="setDate(2)">最近三天</v-btn>
          <v-btn text block left @click="setDate(3)">最近一周</v-btn>
          <v-btn text block left @click="setDate(4)">最近一月</v-btn>
          <v-btn text block left @click="setDate(5)">最近半年</v-btn>
          <v-btn text block left @click="setDate(6)">最近一年</v-btn>
        </v-col>
        <v-col cols="12" sm="5">
          <v-row justify="center">开始日期</v-row>
          <v-row justify="center" class="pt-2">
            <v-date-picker v-model="startPicker" :first-day-of-week="0" locale="zh-cn" no-title></v-date-picker>
          </v-row>
        </v-col>
        <v-col cols="12" sm="5">
          <v-row justify="center">结束日期</v-row>
          <v-row justify="center" class="pt-2">
            <v-date-picker v-model="endPicker" :first-day-of-week="0" locale="zh-cn" no-title></v-date-picker>
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
    dateRangeText() {
      this.dates = [this.startPicker, this.endPicker];
      if (this.startPicker == null || !this.endPicker == null) {
        return "";
      }
      return this.dates.join(" ~ ");
    }
  },
  methods: {
    setDate(param) {
      switch (param) {
        case 1:
          this.startPicker = new Date().toISOString().substr(0, 10);
          this.endPicker = new Date().toISOString().substr(0, 10);
          break;
        case 2:
          this.startPicker = subDays(new Date(), 3)
            .toISOString()
            .substr(0, 10);
          this.endPicker = new Date().toISOString().substr(0, 10);
          break;
        case 3:
          this.startPicker = subDays(new Date(), 7)
            .toISOString()
            .substr(0, 10);
          this.endPicker = new Date().toISOString().substr(0, 10);
          break;
        case 4:
          this.startPicker = subDays(new Date(), 30)
            .toISOString()
            .substr(0, 10);
          this.endPicker = new Date().toISOString().substr(0, 10);
          break;
        case 5:
          this.startPicker = subDays(new Date(), 180)
            .toISOString()
            .substr(0, 10);
          this.endPicker = new Date().toISOString().substr(0, 10);
          break;
        case 6:
          this.startPicker = subDays(new Date(), 360)
            .toISOString()
            .substr(0, 10);
          this.endPicker = new Date().toISOString().substr(0, 10);
          break;
        default:
          this.startPicker = null;
          this.endPicker = null;
      }
    }
  },
  mounted() {
    console.log(new Date());
  }
};
</script>