package edu.neu.social.dao;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import edu.neu.social.entity.po.NewsSort;
import edu.neu.social.entity.po.User;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

/**
 * <p>
 * 新闻分类 Mapper 接口
 * </p>
 *
 * @author halozhy
 */
@Mapper
public interface NewsSortMapper extends BaseMapper<NewsSort> {

}
