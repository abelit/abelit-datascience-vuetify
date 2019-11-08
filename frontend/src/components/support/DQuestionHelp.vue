<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ on }">
      <v-btn icon v-on="on">
        <v-icon>contact_support</v-icon>
      </v-btn>
    </template>
    <span>{{ $vuetify.lang.t("$vuetify.tooltip.questionHelp") }}</span>
  </v-tooltip>
</template>
