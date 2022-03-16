package edu.neu.social.entity.po;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.ToString;

import java.io.Serializable;

/**
 * <p>
 * 新闻类别
 * </p>
 *
 * @author halozhy
 */
@Data
@EqualsAndHashCode(callSuper = false)
@ToString
@TableName("t_news_sort")
public class NewsSort implements Serializable {

    private static final long serialVersionUID = 1L;

    @TableId(value = "id", type = IdType.AUTO)
    private Long id;

    private String content;
}
