<template>
  <v-menu offset-y origin="center center">
    <template v-slot:activator="{ on: menu }">
      <v-tooltip bottom>
        <template v-slot:activator="{ on: tooltip }">
          <v-btn icon v-on="{ ...tooltip, ...menu }">
            <v-avatar size="24">
              <img :src="userPortrait" alt="User Portrait" />
            </v-avatar>
          </v-btn>
        </template>
        <span>Im A ToolTip</span>
      </v-tooltip>
    </template>
    <v-list>
      <v-list-item v-for="(item, index) in items" :key="index" @click>
        <v-list-item-title>{{ item.title }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-menu>
</template>


<script>
export default {
  data: () => ({
    userPortrait: "/static/images/portrait/portrait_male_007.jpg",
    items: [
      { title: "Click Me1       ewqrqw werqew" },
      { title: "Click Me2" },
      { title: "Click Me3" },
      { title: "Click Me4" }
    ]
  })
};
</script>