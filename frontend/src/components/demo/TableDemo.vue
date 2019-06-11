<template>
  <v-container grid-list-xs fluid>
    <v-layout row wrap>
      <v-flex xs12 dark>
        <table
          id="user-table"
          class="display table-bordered nowrap testt"
          cellspacing="0"
          width="100%"
        >
          <thead>
            <tr>
              <th>User ID</th>
              <th>User Name</th>
              <th>User Email</th>
            </tr>
          </thead>
          <tbody></tbody>
        </table>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    id: "",
    name: "",
    email: "",
    dataTable: null
  }),
  methods: {
  },
  mounted() {
    let users = [];

    this.dataTable = $("#user-table").DataTable({
      dom: 'B<"clear">frtip',
      buttons: [
        {
          extend: "collection",
          text: '<i class="fa fa-ellipsis-h"></i>',
          buttons: [
            "copyHtml5",
            "excelHtml5",
            "csvHtml5",
            "pdfHtml5",
            {
              extend: "excelHtml5",
              text: '<i class="fa fa-file-excel-o"></i>',
              titleAttr: this.$t("table.export") + "Excel"
            }
          ],
          fade: true
        }
      ],
      language: {
        paginate: {
          first: "首页",
          previous: "上一页",
          next: "下一页",
          last: "最后一页"
        },
        excel: "导出excel"
      }
    });
    const url = "https://jsonplaceholder.typicode.com/users";
    fetch(url)
      .then(res => res.json())
      .then(data => {
        data.forEach(item => {
          users.push(item);
        });

        users.forEach(user => {
          this.dataTable.row
            .add([user.id, '<a href="#">' + user.name + "</a>", user.email])
            .draw(false);
        });
      });
  }
};
</script>


<style>
div.dt-buttons {
  position: relative;
  float: right;
}
</style>
