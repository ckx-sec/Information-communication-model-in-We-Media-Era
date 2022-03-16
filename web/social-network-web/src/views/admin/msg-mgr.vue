<template>
  <div class="app-container">
    <div class="filter-container" style="margin-bottom: 1rem"></div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%"
    >
      <template slot="empty"> 暂无数据 </template>
      <el-table-column
        label="ID"
        prop="id"
        sortable
        align="center"
        min-width="80"
      >
        <template slot-scope="{ row }">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="新闻类别" min-width="700px" align="center">
        <template slot-scope="{ row }">
          <span>{{ row.content }}</span>
        </template>
      </el-table-column>
      <el-table-column
        label="操作"
        align="center"
        min-width="150px"
        class-name="small-padding fixed-width"
      >
        <template slot-scope="{ row }">
          <el-button type="primary" size="mini" @click="handleSeeNews(row)">
            查看
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog title="相关新闻" :visible.sync="dialogSeeNewsVisible" top="15vh">
      <el-table
        v-loading="listLoadingContent"
        :data="listContent"
        border
        fit
        highlight-current-row
        style="width: 200%"
        max-height="400"
      >
        <el-table-column
          label="ID"
          prop="id"
          sortable
          align="center"
          min-width="80"
        >
          <template slot-scope="{ row }">
            <span>{{ row.id }}</span>
          </template>
        </el-table-column>
        <el-table-column label="内容" min-width="100px" align="center">
          <template slot-scope="{ row }">
            <span>{{ row.content }}</span>
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
  </div>
</template>

<script>
// import { fetchList, fetchPv, createArticle, updateArticle } from '@/api/article'
import waves from "@/directive/waves"; // waves directive
import { parseTime } from "@/utils";
import Pagination from "@/components/Pagination"; // secondary package based on el-pagination

const calendarTypeOptions = [
  { key: "CN", display_name: "China" },
  { key: "US", display_name: "USA" },
  { key: "JP", display_name: "Japan" },
  { key: "EU", display_name: "Eurozone" },
];

const calendarTypeKeyValue = calendarTypeOptions.reduce((acc, cur) => {
  acc[cur.key] = cur.display_name;
  return acc;
}, {});

export default {
  name: "MsgMgr",
  components: { Pagination },
  directives: { waves },
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: "success",
        draft: "info",
        deleted: "danger",
      };
      return statusMap[status];
    },
    typeFilter(type) {
      return calendarTypeKeyValue[type];
    },
  },
  data() {
    return {
      tableKey: 0,
      list: null,
      listContent: null,
      total: 0,
      listLoading: true,
      listLoadingContent: true,
      listQuery: {
        id: "",
        name: "",
        username: "",
        page: 1,
        limit: 20,
        importance: undefined,
        title: undefined,
        type: undefined,
        sort: "+id",
      },
      importanceOptions: [1, 2, 3],
      calendarTypeOptions,
      sortOptions: [
        { label: "ID 升序", key: "+id" },
        { label: "ID 降序", key: "-id" },
      ],
      statusOptions: ["published", "draft", "deleted"],
      showReviewer: false,
      temp: {
        username: "",
        password: "",
        name: "",
        contact: "",
        type: 1,
        fac_name: "",
        fac_describe: "",
      },
      dialogFormVisible: false,
      dialogStatus: "",
      textMap: {
        update: "更改",
        create: "添加",
      },
      dialogSeeNewsVisible: false,
      dialogUpdateFormVisible: false,
      pvData: [],
      rules: {
        type: [
          { required: true, message: "type is required", trigger: "change" },
        ],
        timestamp: [
          {
            type: "date",
            required: true,
            message: "timestamp is required",
            trigger: "change",
          },
        ],
        title: [
          { required: true, message: "title is required", trigger: "blur" },
        ],
      },
      downloadLoading: false,
    };
  },
  created() {
    this.getList();
  },
  methods: {
    handleSeeNews(row) {
      this.selectedRow = row;
      this.dialogSeeNewsVisible = true;
      console.log(row.id);
      this.getNewsContentList(row.id);
    },
    getNewsContentList(sort_id) {
      this.listLoadingContent = true;
      // this.list = response.data.items
      var q = { sort_id: sort_id };

      this.$axios.post("/api/news_content/list", q).then((r) => {
        this.listContent = r.data;

        // this.list = this.temp
        console.log(r.data);
        // this.total = r.data.count
        this.listLoadingContent = false;
      });
    },
    getList() {
      this.listLoading = true;
      this.$axios.post("/api/news_sort/list", this.listQuery).then((r) => {
        this.list = r.data;
        console.log(r.data);
        this.listLoading = false;
      });
    },
    handleFilter() {
      this.listQuery.page = 1;
      this.getList();
    },
    handleModifyStatus(row, status) {
      this.$message({
        message: "操作Success",
        type: "success",
      });
      row.status = status;
    },
    resetTemp() {
      this.temp = {
        username: "",
        password: "",
        name: "",
        contact: "",
        type: 1,
        fac_name: "",
        fac_describe: "",
      };
    },
    handleCreate() {
      this.resetTemp();
      this.dialogStatus = "create";
      this.dialogFormVisible = true;
      this.$nextTick(() => {
        this.$refs["dataForm"].clearValidate();
      });
    },
    createData() {
      this.$axios.post("/api/user/add", this.temp).then((r) => {
        if (r.data === -2) {
          this.$message.error("表单未填写完整");
        } else if (r.data === -1) {
          this.$message.error("用户名重复");
        } else if (r.data === 0) {
          this.$message.success("添加成功");
          this.dialogFormVisible = false;
          this.handleReFresh();
        }
      });
      console.log(this.temp);
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, row); // copy obj
      this.dialogUpdateFormVisible = true;
      this.$nextTick(() => {
        this.$refs["dataForm"].clearValidate();
      });
    },
    updateData() {
      this.$axios.post("/api/user/update", this.temp).then((r) => {
        if (r.data === -2) {
          this.$message.error("表单未填写完整");
        } else if (r.data === -1) {
          this.$message.error("无此用户");
        } else if (r.data === 0) {
          this.$message.success("更改成功");
          this.dialogUpdateFormVisible = false;
          this.handleReFresh();
        }
      });
    },
    handleDelete(row, index) {
      this.$confirm("此操作将删除该用户, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.$axios
            .get("/api/user/delete", {
              params: {
                uId: row.id,
              },
            })
            .then((r) => {
              // 0 ok -1 此用户下仍有未完成的订单 -2 无此用户
              if (r.data === -2) {
                this.$message.error("无此用户");
              } else if (r.data === -1) {
                this.$message.error("无法删除，此用户下仍有未完成的订单");
              } else if (r.data === 0) {
                this.$message.success("删除成功");
                this.handleReFresh();
              }
            });
        })
        .catch(() => {
        });
    },
    handleReFresh() {
      this.listQuery.id = null;
      this.listQuery.username = null;
      this.listQuery.name = null;
      // this.listQuery.page = 1
      this.getList();
    },
    formatJson(filterVal) {
      return this.list.map((v) =>
        filterVal.map((j) => {
          if (j === "timestamp") {
            return parseTime(v[j]);
          } else {
            return v[j];
          }
        })
      );
    },
  },
};
</script>
