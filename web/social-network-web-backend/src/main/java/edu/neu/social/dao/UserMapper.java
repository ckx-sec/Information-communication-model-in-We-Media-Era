package edu.neu.social.dao;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import edu.neu.social.entity.po.User;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

/**
 * <p>
 * 用户 Mapper 接口
 * </p>
 *
 * @author halozhy
 * @since 2021-07-15
 */
@Mapper
public interface UserMapper extends BaseMapper<User> {

    @Select("select * from t_user where u_username = #{uName}")
    User selectByName(String uName);

    @Select("select * from t_user ${ew.customSqlSegment} limit #{offset}, #{limit}")
    List<User> listPage(int offset, int limit, QueryWrapper ew);
}
