<template>
  <div>
    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <div v-on="on">
          <v-tooltip bottom>
        <template v-slot:activator="{ on }">
        <v-btn color="transparent" v-on="on" icon>
          <img v-if="language" :src="require('@/assets/images/auth/'+language+'.png')" alt>
        </v-btn>
      </template>
      <span>{{ $t("tooltip.LANG_SWITCH") }}</span>
      </v-tooltip>
        </div>
      </template>
      <v-list>
        <v-list-tile
          v-for="(lang, index) in langList"
          :key="index"
          :disabled="language === lang.code"
        >
          <v-list-tile-avatar>
            <v-avatar size="32px" tile @click="setLanguage(lang.code)">
              <img :src="require('@/assets/images/auth/'+lang.code+'.png')" alt="language">
            </v-avatar>
          </v-list-tile-avatar>
          <v-list-tile-title @click="setLanguage(lang.code)">{{ lang.name }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-menu>
  </div>
</template>


<script>
export default {
  data: () => ({
    language: "",
    langList: [
      {
        code: "zh_CN",
        name: "简体中文"
      },
      {
        code: "en_US",
        name: "English"
      }
    ]
  }),
  methods: {
    // 语言切换
    setLanguage(lang) {
      this.language = lang;
      // 设置国际化语言信息
      this.$i18n.locale = lang;
      // 设置验证语言信息
      this.$validator.locale = lang;

      // 通过异步方式调用store中setLanguage方法，保存语言信息
      this.$store.dispatch("setLanguage", lang);

      console.log(this.language);
    }
  },
  mounted() {
    // 从vuex中获取语言信息
    this.language = this.$store.state.language;
  }
};
</script>