<template>
  <v-menu
    offset-y
    origin="center center"
    class="elelvation-1"
    :nudge-bottom="14"
    transition="scale-transition"
  >
    <template v-slot:activator="{ on }">
      <v-btn icon flat v-on="on">
        <v-badge color="red" overlap>
          <template v-slot:badge>
            <span>3</span>
          </template>

          <v-icon medium>notifications</v-icon>
        </v-badge>
      </v-btn>
    </template>
    <!-- <notification-list></notification-list> -->
  </v-menu>
</template>
