package edu.neu.social.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import edu.neu.social.dao.NewsContentMapper;
import edu.neu.social.dao.NewsSortMapper;
import edu.neu.social.entity.po.NewsContent;
import edu.neu.social.entity.po.NewsSort;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * <p>
 * 新闻 服务实现类
 * </p>
 *
 * @author halozhy
 */
@Slf4j
@Service
public class NewsContentService extends ServiceImpl<NewsContentMapper, NewsContent> implements IService<NewsContent> {
    @Autowired
    NewsContentMapper newsContentMapper;

}


