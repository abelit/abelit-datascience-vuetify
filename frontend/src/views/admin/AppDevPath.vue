<template>
  <v-container>
    <v-row>
      <v-col>
        <v-timeline>
          <v-timeline-item v-for="item in items" :key="item.id" color="red lighten-2" large>
            <template v-slot:opposite>
              <span>{{item.date}}</span>
            </template>
            <v-card class="elevation-2">
              <v-card-title class="headline">{{item.title}}</v-card-title>
              <v-card-text>{{item.content}}</v-card-text>
            </v-card>
          </v-timeline-item>
        </v-timeline>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
        items: [{
            id: 1,
            date: "2019-Q4",
            title: "Base Layout",
            content: "Design base layout based on vue and vuetify, and design backend structure based on Flask."
        },
        {
            id: 2,
            date: "2020-Q1",
            title: "Login based flask token and Wechat Login",
            content: "To login backend based flask token, and complete tag dispaly on content page, and complete wechat login."
        }]
    }
  }
};
</script>