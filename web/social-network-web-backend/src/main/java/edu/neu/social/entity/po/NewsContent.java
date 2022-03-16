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
 * 新闻
 * </p>
 *
 * @author halozhy
 */
@Data
@EqualsAndHashCode(callSuper = false)
@ToString
@TableName("t_news_content")
public class NewsContent implements Serializable {

    private static final long serialVersionUID = 1L;

    private Long id;

    private Long sort_id;

    private String content;
}
