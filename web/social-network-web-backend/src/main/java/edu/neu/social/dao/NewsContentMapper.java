package edu.neu.social.dao;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import edu.neu.social.entity.po.NewsContent;
import edu.neu.social.entity.po.NewsSort;
import org.apache.ibatis.annotations.Mapper;

/**
 * <p>
 * 新闻 Mapper 接口
 * </p>
 *
 * @author halozhy
 */
@Mapper
public interface NewsContentMapper extends BaseMapper<NewsContent> {

}
