package edu.neu.social.entity.vo;

import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.ToString;

import java.io.Serializable;

/**
 * <p>
 * 用户Vo
 * </p>
 *
 * @author halozhy
 */
@Data
@EqualsAndHashCode(callSuper = false)
@ToString
public class UserVo implements Serializable {

    private static final long serialVersionUID = 1L;

    private Long id;

    private String username;

    private String password;

    private String name;

    private String contact;

}
