package edu.neu.social.entity.po;

import com.baomidou.mybatisplus.annotation.*;

import java.io.Serializable;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.ToString;

/**
 * <p>
 * 用户
 * </p>
 *
 * @author halozhy
 */
@Data
@EqualsAndHashCode(callSuper = false)
@ToString
@TableName("t_user")
public class User implements Serializable {

    private static final long serialVersionUID = 1L;

    @TableId(value = "u_id", type = IdType.AUTO)
    private Long uId;

    private String uUsername;

    private String uPassword;

    private String uName;

    private String uContact;

}
