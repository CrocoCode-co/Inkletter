from inkletter.md_to_mjml import parse_markdown_to_mjml, wrap_mjml_body


def test_md_generation_full_syntax(ast):
    markdown_input = """\
# 📣 **New Product Launch Campaign** — *Spring 2025*

Welcome to our official campaign brief for the **MegaWidget 5000**.  
Let's make this launch unforgettable!

---

## 🚀 Campaign Goals

- **Raise awareness** about MegaWidget 5000.
- **Drive pre-orders** during the launch month.
- **Engage influencers and reviewers**.

---

## 📅 Timeline

| Phase          | Start Date | End Date   |
|----------------|------------|------------|
| Planning       | 2025-04-01 | 2025-04-15 |
| Teaser Phase   | 2025-04-16 | 2025-04-30 |
| Launch Phase   | 2025-05-01 | 2025-05-31 |
| Follow-up      | 2025-06-01 | 2025-06-15 |

---

## 📌 Key Actions

### Pre-Launch

- [x] Define target audience
- [x] Finalize product specs
- [ ] Build landing page
- [ ] Send teaser emails

### Launch Week

- [ ] Go live on website
- [ ] Announce on **social media**
- [ ] Release press release
- [ ] Partner with influencers

### Post-Launch

- [ ] Gather reviews
- [ ] Run retargeting ads
- [ ] Send thank-you emails

---

## 💬 Messaging Examples

> "**Revolutionize your workflow** — Meet the MegaWidget 5000."
>
> _"Faster, smarter, better. The tool you didn't know you needed."_

---

## 📧 Email Snippet

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>Introducing the MegaWidget 5000 🚀</h1>
    <p>Pre-order now and get 20% off + free shipping!</p>
  </body>
</html>
```
"""

    expected = """\
<mjml>
  <mj-body>
    <mj-section>
      <mj-column>
        <mj-text>
          <h1>📣 <strong>New Product Launch Campaign</strong> — <em>Spring 2025</em></h1>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          Welcome to our official campaign brief for the <strong>MegaWidget 5000</strong>.<br/>
          Let's make this launch unforgettable!
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-divider border-color="#cccccc" border-width="1px"/>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          <h2>🚀 Campaign Goals</h2>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          <ul>
            <li>
              <strong>Raise awareness</strong> about MegaWidget 5000.
            </li>
            <li>
              <strong>Drive pre-orders</strong> during the launch month.
            </li>
            <li>
              <strong>Engage influencers and reviewers</strong>.
            </li>
          </ul>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-divider border-color="#cccccc" border-width="1px"/>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          <h2>📅 Timeline</h2>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-table>
          <tr>
            <th>Phase</th>
            <th>Start Date</th>
            <th>End Date</th>
          </tr>
          <tr>
            <td>Planning</td>
            <td>2025-04-01</td>
            <td>2025-04-15</td>
          </tr>
          <tr>
            <td>Teaser Phase</td>
            <td>2025-04-16</td>
            <td>2025-04-30</td>
          </tr>
          <tr>
            <td>Launch Phase</td>
            <td>2025-05-01</td>
            <td>2025-05-31</td>
          </tr>
          <tr>
            <td>Follow-up</td>
            <td>2025-06-01</td>
            <td>2025-06-15</td>
          </tr>
        </mj-table>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-divider border-color="#cccccc" border-width="1px"/>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          <h2>📌 Key Actions</h2>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          <h3>Pre-Launch</h3>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          <ul style="list-style-type: none;">
            <li>
              ☑ Define target audience
            </li>
            <li>
              ☑ Finalize product specs
            </li>
            <li>
              ☐ Build landing page
            </li>
            <li>
              ☐ Send teaser emails
            </li>
          </ul>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          <h3>Launch Week</h3>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          <ul style="list-style-type: none;">
            <li>
              ☐ Go live on website
            </li>
            <li>
              ☐ Announce on <strong>social media</strong>
            </li>
            <li>
              ☐ Release press release
            </li>
            <li>
              ☐ Partner with influencers
            </li>
          </ul>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          <h3>Post-Launch</h3>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          <ul style="list-style-type: none;">
            <li>
              ☐ Gather reviews
            </li>
            <li>
              ☐ Run retargeting ads
            </li>
            <li>
              ☐ Send thank-you emails
            </li>
          </ul>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-divider border-color="#cccccc" border-width="1px"/>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          <h2>💬 Messaging Examples</h2>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text font-style="italic" color="#555555">
          "<strong>Revolutionize your workflow</strong> — Meet the MegaWidget 5000."<em>"Faster, smarter, better. The tool you didn't know you needed."</em>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-divider border-color="#cccccc" border-width="1px"/>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          <h2>📧 Email Snippet</h2>
        </mj-text>
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text>
          <pre>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
  &lt;body&gt;
    &lt;h1&gt;Introducing the MegaWidget 5000 🚀&lt;/h1&gt;
    &lt;p&gt;Pre-order now and get 20% off + free shipping!&lt;/p&gt;
  &lt;/body&gt;
&lt;/html&gt;
          </pre>
        </mj-text>
      </mj-column>
    </mj-section>
  </mj-body>
</mjml>"""

    actual = parse_markdown_to_mjml(markdown_input)
    print("actual:")
    print(actual)
    print("expected:")
    print(expected)
    assert actual == expected
