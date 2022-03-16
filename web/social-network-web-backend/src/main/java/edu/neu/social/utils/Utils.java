package edu.neu.social.utils;

import com.alibaba.fastjson.JSONObject;
import org.apache.commons.collections4.ListUtils;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Utils {
    /**
     * 验证字段是否非空
     * @param jsonObject 提交的JSON对象
     * @param notEmptyNameList 一个 List String 类型的数组，里面是要验证非空的字段名
     * @return true 表示字段均为非空，false 存在空字段
     */
    public static boolean checkEmpty(JSONObject jsonObject, List<String> notEmptyNameList) {
        for (Map.Entry<String, Object> stringObjectEntry : jsonObject.entrySet()) {
            if (notEmptyNameList.contains(stringObjectEntry.getKey()) &&
                    String.valueOf(stringObjectEntry.getValue()).isEmpty()) {
                return false;
            }
        }
        return true;
    }

    /**
     * 把 element ui 日期时间选择器默认返回的时间格式字符串格式化成 LocalDateTime
     * 注意 后端采用的 LocalDateTime 和 前端的日期选择器会有8小时时差，需要手动补加上去
     * @param s element ui 日期时间选择器默认返回的时间格式字符串，应该是 2019-02-10T11:21:25.346Z 这种的
     * @return LocalDateTime
     */
    public static LocalDateTime parseToLocalDateTime(String s){
         s = s.substring(0, s.length() - 5);
         return LocalDateTime.parse(s).plusHours(8);
    }

    /**
     * 把 element ui 日期选择器默认返回的时间格式字符串格式化成 LocalDate
     * 注意 后端采用的 LocalDateTime 和 前端的日期选择器会有8小时时差，需要手动补加上去
     * @param s element ui 日期选择器默认返回的时间格式字符串，应该是 2021-06-30T16:00:00.000Z 这种的
     * @return LocalDateTime
     */
    public static LocalDate parseToLocalDate(String s){
//        s = s.substring(0, s.length() - 14);
        s = s.substring(0, s.length() - 5);

        LocalDateTime localDateTime = LocalDateTime.parse(s).plusHours(8);
        return localDateTime.toLocalDate();
    }

    /**
     * 如果limit加wrapper实现分页不好使了，不妨自己来分页
     * @param origin 原始数据
     * @param page 第page页
     * @param limit 每页limit个
     * @param <T> 实体类类型
     * @return 第page页的List数据
     */
    public static <T> List<T> pageByMe(List<T> origin, int page ,int limit){
        List<List<T>> partition = ListUtils.partition(origin, limit);
        List<T> result = new ArrayList<>();
        for (int i = 0; i < partition.size(); i++) {
            if (page == i + 1) {
                result = partition.get(i);
                break;
            }
        }
        return result;
    }
}
